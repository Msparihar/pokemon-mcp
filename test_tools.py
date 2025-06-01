"""
Test script for Pokemon MCP tools using async MCP client.
"""

import asyncio
import json
import logging
from contextlib import AsyncExitStack
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any, Optional

from mcp import ClientSession
from mcp.client.sse import sse_client

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")


class MCPTester:
    """Class to handle MCP tool testing."""

    def __init__(self):
        """Initialize the tester."""
        self.session = None
        self.exit_stack = AsyncExitStack()
        self.results_dir = Path(__file__).parent / "test_results"
        self.results_dir.mkdir(parents=True, exist_ok=True)
        self.test_results = []

    async def connect(self):
        """Connect to the MCP server."""
        logging.info("Connecting to MCP server...")
        try:
            stdio_transport = await self.exit_stack.enter_async_context(sse_client("http://localhost:8050/sse"))
            stdio, write = stdio_transport
            self.session = await self.exit_stack.enter_async_context(ClientSession(stdio, write))
            await self.session.initialize()

            tools_result = await self.session.list_tools()
            logging.info("Available tools:")
            for tool in tools_result.tools:
                logging.info(f"  - {tool.name}: {tool.description}")

            logging.info("Successfully connected to MCP server")
        except Exception as e:
            logging.error(f"Failed to connect to MCP server: {str(e)}")
            raise

    async def test_tool(self, tool_name: str, params: dict) -> Any:
        """Test a specific tool."""
        try:
            logging.info(f"\nTesting {tool_name}...")
            logging.info(f"Parameters: {json.dumps(params, indent=2)}")

            result = await self.session.call_tool(tool_name, params)
            data = json.loads(result.content[0].text)
            logging.info(f"Result:\n{json.dumps(data, indent=2)}")

            # Store test result
            self.test_results.append(
                {"tool": tool_name, "parameters": params, "result": data, "timestamp": datetime.now().isoformat()}
            )

            return data

        except Exception as e:
            error_data = {"error": str(e), "tool": tool_name, "parameters": params}
            self.test_results.append(
                {"tool": tool_name, "parameters": params, "result": error_data, "timestamp": datetime.now().isoformat()}
            )
            logging.error(f"Tool execution failed: {str(e)}")
            raise

    async def save_results(self):
        """Save test results to a JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = self.results_dir / f"test_results_{timestamp}.json"

        results = {
            "timestamp": datetime.now().isoformat(),
            "total_tests": len(self.test_results),
            "tests": self.test_results,
        }

        with open(results_file, "w") as f:
            json.dump(results, f, indent=2)

        logging.info(f"Test results saved to: {results_file}")

    async def cleanup(self):
        """Clean up resources."""
        await self.exit_stack.aclose()


async def run_tests():
    """Run all tool tests."""
    tester = MCPTester()
    await tester.connect()

    try:
        # Test type effectiveness first
        logging.info("\nTesting Type Effectiveness")
        logging.info("=" * 50)

        await tester.test_tool(
            "get_type_effectiveness",
            {
                "attacking_type": "Fire",
                "defending_types": ["Grass", "Steel"],
                "context": "Checking STAB Fire move against Ferrothorn",
            },
        )

        # Test team building tools
        logging.info("\nTesting Team Building Tools")
        logging.info("=" * 50)

        await tester.test_tool(
            "build_balanced_team",
            {"core_pokemon": "Charizard", "format": "OU", "style": "offensive", "excluded_types": ["Ground"]},
        )

        await tester.test_tool(
            "get_team_archetype", {"archetype": "rain", "format": "OU", "key_pokemon": "Pelipper", "style": "balanced"}
        )

        # Test battle analysis tools
        logging.info("\nTesting Battle Analysis Tools")
        logging.info("=" * 50)

        await tester.test_tool(
            "predict_matchup",
            {
                "team1": ["Charizard", "Tyranitar", "Excadrill"],
                "team2": ["Swampert", "Ferrothorn", "Garchomp"],
                "format": "OU",
                "scoring_priority": "type_advantage",
            },
        )

        # Save all test results
        await tester.save_results()

    finally:
        await tester.cleanup()


def main():
    """Main entry point."""
    try:
        asyncio.run(run_tests())
    except KeyboardInterrupt:
        logging.info("Test interrupted by user")
    except Exception as e:
        logging.error(f"Test failed: {str(e)}", exc_info=True)


if __name__ == "__main__":
    main()
