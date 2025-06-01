# server.py
from mcp.server.fastmcp import FastMCP
import requests
import json
from typing import Dict, Any, Optional, List
from modules.battle_analyzer import BattleAnalyzer
from modules.team_builder import TeamBuilder
from modules.team_archetypes import TeamArchetypes
from utils.type_calculator import TypeCalculator

# Create an MCP server
mcp = FastMCP(
    name="Pokemon MCP Server",
    host="0.0.0.0",
    port=8050,
)

battle_analyzer = BattleAnalyzer()
team_builder = TeamBuilder()
team_archetypes = TeamArchetypes()
type_calculator = TypeCalculator()

# Base URL for PokéAPI
POKEAPI_BASE = "https://pokeapi.co/api/v2"


def fetch_pokemon_data(endpoint: str) -> Optional[Dict[str, Any]]:
    """Helper function to fetch data from PokéAPI"""
    try:
        response = requests.get(f"{POKEAPI_BASE}/{endpoint}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data: {str(e)}"}


# Competitive Analysis Tools
@mcp.tool()
def get_type_effectiveness(attacking_type: str, defending_types: List[str], context: str = "") -> Dict[str, Any]:
    """Get detailed type effectiveness analysis."""
    return type_calculator.get_effectiveness(attacking_type, defending_types)


@mcp.tool()
def build_balanced_team(
    core_pokemon: str, format: str = "OU", style: str = "balanced", excluded_types: List[str] = None
) -> Dict[str, Any]:
    """Build a balanced team around a core Pokemon."""
    return team_builder.build_team(core_pokemon, format, style, excluded_types or [])


@mcp.tool()
def get_team_archetype(
    archetype: str, format: str = "OU", key_pokemon: Optional[str] = None, style: str = "balanced"
) -> Dict[str, Any]:
    """Get team suggestions for specific archetypes."""
    return team_archetypes.get_team_suggestion(archetype, format, key_pokemon, style)


@mcp.tool()
def predict_matchup(
    team1: List[str], team2: List[str], format: str = "OU", scoring_priority: str = "overall"
) -> Dict[str, Any]:
    """Predict battle outcome between two teams."""
    return battle_analyzer.predict_matchup(team1, team2, format, scoring_priority)


# Pokemon Data Tools
@mcp.tool()
def get_pokemon(name_or_id: str) -> Dict[str, Any]:
    """Get detailed information about a specific Pokémon by name or ID"""
    return fetch_pokemon_data(f"pokemon/{name_or_id.lower()}")


@mcp.tool()
def get_pokemon_species(name_or_id: str) -> Dict[str, Any]:
    """Get species information about a Pokémon including flavor text and evolution chain"""
    return fetch_pokemon_data(f"pokemon-species/{name_or_id.lower()}")


@mcp.tool()
def get_pokemon_ability(name_or_id: str) -> Dict[str, Any]:
    """Get information about a specific Pokémon ability"""
    return fetch_pokemon_data(f"ability/{name_or_id.lower()}")


@mcp.tool()
def get_pokemon_move(name_or_id: str) -> Dict[str, Any]:
    """Get information about a specific Pokémon move"""
    return fetch_pokemon_data(f"move/{name_or_id.lower()}")


@mcp.tool()
def get_pokemon_type(name_or_id: str) -> Dict[str, Any]:
    """Get information about a Pokémon type including damage relations"""
    return fetch_pokemon_data(f"type/{name_or_id.lower()}")


@mcp.tool()
def search_pokemon(limit: int = 20, offset: int = 0) -> Dict[str, Any]:
    """Search and list Pokémon with pagination"""
    return fetch_pokemon_data(f"pokemon?limit={limit}&offset={offset}")


@mcp.tool()
def get_evolution_chain(chain_id: int) -> Dict[str, Any]:
    """Get evolution chain information by chain ID"""
    return fetch_pokemon_data(f"evolution-chain/{chain_id}")


@mcp.tool()
def get_pokemon_location_encounters(name_or_id: str) -> Dict[str, Any]:
    """Get location areas where a Pokémon can be encountered"""
    return fetch_pokemon_data(f"pokemon/{name_or_id.lower()}/encounters")


@mcp.tool()
def get_generation(name_or_id: str) -> Dict[str, Any]:
    """Get information about a specific Pokémon generation"""
    return fetch_pokemon_data(f"generation/{name_or_id.lower()}")


@mcp.tool()
def compare_pokemon_stats(pokemon1: str, pokemon2: str) -> Dict[str, Any]:
    """Compare base stats between two Pokémon"""
    data1 = fetch_pokemon_data(f"pokemon/{pokemon1.lower()}")
    data2 = fetch_pokemon_data(f"pokemon/{pokemon2.lower()}")

    if "error" in data1 or "error" in data2:
        return {"error": "Failed to fetch one or both Pokémon"}

    stats_comparison = {
        "pokemon1": {
            "name": data1["name"],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data1["stats"]},
        },
        "pokemon2": {
            "name": data2["name"],
            "stats": {stat["stat"]["name"]: stat["base_stat"] for stat in data2["stats"]},
        },
        "differences": {},
    }

    for stat_name in stats_comparison["pokemon1"]["stats"]:
        diff = stats_comparison["pokemon2"]["stats"][stat_name] - stats_comparison["pokemon1"]["stats"][stat_name]
        stats_comparison["differences"][stat_name] = diff

    return stats_comparison


# Resource Formatters
@mcp.resource("pokemon://{name_or_id}")
def get_pokemon_resource(name_or_id: str) -> str:
    """Get Pokémon data as a formatted resource"""
    data = fetch_pokemon_data(f"pokemon/{name_or_id.lower()}")

    if "error" in data:
        return f"Error: {data['error']}"

    return f"""
# {data['name'].title()} (#{data['id']})

**Height:** {data['height']/10} m
**Weight:** {data['weight']/10} kg
**Base Experience:** {data['base_experience']}

## Types
{', '.join([t['type']['name'].title() for t in data['types']])}

## Abilities
{', '.join([a['ability']['name'].title() for a in data['abilities']])}

## Base Stats
{chr(10).join([f"- **{stat['stat']['name'].title()}:** {stat['base_stat']}" for stat in data['stats']])}

## Sprites
- Front Default: {data['sprites']['front_default']}
- Front Shiny: {data['sprites']['front_shiny']}
"""


@mcp.resource("pokemon-move://{name_or_id}")
def get_move_resource(name_or_id: str) -> str:
    """Get Pokémon move data as a formatted resource"""
    data = fetch_pokemon_data(f"move/{name_or_id.lower()}")

    if "error" in data:
        return f"Error: {data['error']}"

    effect_text = ""
    if data.get("effect_entries"):
        effect_text = data["effect_entries"][0]["effect"]

    return f"""
# {data['name'].title()}

**Type:** {data['type']['name'].title()}
**Power:** {data.get('power', 'N/A')}
**Accuracy:** {data.get('accuracy', 'N/A')}
**PP:** {data.get('pp', 'N/A')}
**Damage Class:** {data['damage_class']['name'].title()}

## Effect
{effect_text}

## Target
{data['target']['name'].title()}
"""


@mcp.resource("pokemon-type://{name_or_id}")
def get_type_resource(name_or_id: str) -> str:
    """Get Pokémon type data with damage relations"""
    data = fetch_pokemon_data(f"type/{name_or_id.lower()}")

    if "error" in data:
        return f"Error: {data['error']}"

    relations = data["damage_relations"]

    return f"""
# {data['name'].title()} Type

## Damage Relations

### Super Effective Against
{', '.join([t['name'].title() for t in relations['double_damage_to']]) or 'None'}

### Not Very Effective Against
{', '.join([t['name'].title() for t in relations['half_damage_to']]) or 'None'}

### No Effect Against
{', '.join([t['name'].title() for t in relations['no_damage_to']]) or 'None'}

### Weak To
{', '.join([t['name'].title() for t in relations['double_damage_from']]) or 'None'}

### Resists
{', '.join([t['name'].title() for t in relations['half_damage_from']]) or 'None'}

### Immune To
{', '.join([t['name'].title() for t in relations['no_damage_from']]) or 'None'}
"""


if __name__ == "__main__":
    mcp.run(transport="sse")
