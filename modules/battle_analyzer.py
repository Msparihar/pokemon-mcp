"""
Battle analyzer module that provides data for Pokemon battle analysis.
"""

from typing import List, Dict, Any
from utils.type_calculator import TypeCalculator
from pathlib import Path
import json
import requests


class BattleAnalyzer:
    """Provides data for analyzing Pokemon battles."""

    def __init__(self):
        """Initialize with required components."""
        self.type_calculator = TypeCalculator()
        self.pokeapi_base = "https://pokeapi.co/api/v2"
        self.cache_dir = Path(__file__).parent.parent / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def fetch_pokemon_data(self, name: str) -> Dict[str, Any]:
        """Fetch Pokemon data from PokeAPI with caching."""
        cache_file = self.cache_dir / f"{name.lower()}.json"

        if cache_file.exists():
            with open(cache_file, "r") as f:
                return json.load(f)

        try:
            response = requests.get(f"{self.pokeapi_base}/pokemon/{name.lower()}")
            data = response.json()

            pokemon_data = {
                "id": data["id"],
                "name": data["name"],
                "types": [t["type"]["name"] for t in data["types"]],
                "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "moves": [m["move"]["name"] for m in data["moves"]],
            }

            with open(cache_file, "w") as f:
                json.dump(pokemon_data, f, indent=2)

            return pokemon_data

        except Exception as e:
            return {"error": f"Failed to fetch data for {name}: {str(e)}"}

    def predict_matchup(
        self, team1: List[str], team2: List[str], format: str = "OU", scoring_priority: str = "overall"
    ) -> Dict[str, Any]:
        """Provide data for battle matchup analysis."""
        try:
            # Get data for all Pokemon
            team1_data = [self.fetch_pokemon_data(p) for p in team1]
            team2_data = [self.fetch_pokemon_data(p) for p in team2]

            # Get type data for matchup analysis
            team1_types = [p["types"] for p in team1_data if "types" in p]
            team2_types = [p["types"] for p in team2_data if "types" in p]
            type_matchup = self.type_calculator.analyze_team_types(team1_types, team2_types)

            # Get meta context data
            meta_data = self._get_meta_context(format)

            return {
                "team1": {"pokemon": team1_data, "roles": self._get_team_roles(team1_data), "team_types": team1_types},
                "team2": {"pokemon": team2_data, "roles": self._get_team_roles(team2_data), "team_types": team2_types},
                "type_matchup": type_matchup,
                "meta_context": meta_data,
                "format_info": self._get_format_data(format),
                "scoring_priority": scoring_priority,
            }

        except Exception as e:
            return {"error": f"Matchup analysis failed: {str(e)}", "teams": {"team1": team1, "team2": team2}}

    def _get_team_roles(self, team_data: List[Dict[str, Any]]) -> List[str]:
        """Get typical roles based on stats and movesets."""
        roles = []
        for pokemon in team_data:
            if "stats" not in pokemon:
                continue

            stats = pokemon["stats"]
            if stats.get("attack", 0) > stats.get("special-attack", 0):
                if stats.get("speed", 0) > 100:
                    roles.append("physical_sweeper")
                else:
                    roles.append("physical_attacker")
            else:
                if stats.get("speed", 0) > 100:
                    roles.append("special_sweeper")
                else:
                    roles.append("special_attacker")

        return roles

    def _get_meta_context(self, format: str) -> Dict[str, Any]:
        """Get relevant meta game context."""
        return {
            "common_threats": [
                {"pokemon": "Dragapult", "usage": 25.5, "common_moves": ["Dragon Darts", "Shadow Ball"]},
                {"pokemon": "Heatran", "usage": 20.1, "common_moves": ["Magma Storm", "Earth Power"]},
                {"pokemon": "Toxapex", "usage": 19.8, "common_moves": ["Scald", "Toxic"]},
            ],
            "meta_styles": {"hyper_offense": 35, "balance": 40, "stall": 25},
            "speed_control": {"trick_room": 15, "tailwind": 20, "priority": 30, "natural_speed": 35},
        }

    def _get_format_data(self, format: str) -> Dict[str, Any]:
        """Get format-specific data."""
        format_data = {
            "OU": {
                "name": "OverUsed",
                "level_cap": 100,
                "clauses": ["Sleep Clause", "Species Clause", "OHKO Clause", "Evasion Clause", "Endless Battle Clause"],
            },
            "UU": {
                "name": "UnderUsed",
                "level_cap": 100,
                "clauses": ["Sleep Clause", "Species Clause", "OHKO Clause", "Evasion Clause", "Endless Battle Clause"],
            },
        }
        return format_data.get(format.upper(), {"name": format, "description": "Custom format"})
