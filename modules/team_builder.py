"""
Team builder module that provides data for Pokemon team building.
"""

import json
import requests
from pathlib import Path
from typing import List, Dict, Any, Optional
from utils.type_calculator import TypeCalculator


class TeamBuilder:
    """Provides data for building Pokemon teams."""

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
            species_response = requests.get(f"{self.pokeapi_base}/pokemon-species/{name.lower()}")
            species_data = species_response.json()

            pokemon_data = {
                "id": data["id"],
                "name": data["name"],
                "types": [t["type"]["name"] for t in data["types"]],
                "stats": {s["stat"]["name"]: s["base_stat"] for s in data["stats"]},
                "abilities": [a["ability"]["name"] for a in data["abilities"]],
                "moves": [m["move"]["name"] for m in data["moves"]],
                "species_data": {
                    "generation": species_data["generation"]["name"],
                    "growth_rate": species_data["growth_rate"]["name"],
                    "egg_groups": [g["name"] for g in species_data["egg_groups"]],
                },
            }

            with open(cache_file, "w") as f:
                json.dump(pokemon_data, f, indent=2)

            return pokemon_data

        except Exception as e:
            return {"error": f"Failed to fetch data for {name}: {str(e)}"}

    def build_team(
        self, core_pokemon: str, format: str = "OU", style: str = "balanced", excluded_types: List[str] = None
    ) -> Dict[str, Any]:
        """Provide data for building a balanced team."""
        try:
            # Get core Pokemon data
            core_data = self.fetch_pokemon_data(core_pokemon)
            if "error" in core_data:
                return core_data

            # Get type data
            type_data = self.type_calculator.get_pokemon_type_data(core_data["types"])

            # Load format data
            format_data = self._get_format_data(format)

            # Get available Pokemon pool
            pokemon_pool = self._get_pokemon_pool(format)

            return {
                "core_pokemon": {"data": core_data, "type_data": type_data},
                "format_info": format_data,
                "team_style": style,
                "excluded_types": excluded_types or [],
                "pokemon_pool": pokemon_pool,
                "meta_context": self._get_meta_context(format),
            }

        except Exception as e:
            return {"error": f"Team building failed: {str(e)}", "core_pokemon": core_pokemon, "format": format}

    def _get_format_data(self, format: str) -> Dict[str, Any]:
        """Get competitive format data."""
        format_data = {
            "OU": {
                "name": "OverUsed",
                "level_cap": 100,
                "usage_threshold": 4.52,
                "clauses": ["Sleep Clause", "Species Clause", "OHKO Clause", "Evasion Clause", "Endless Battle Clause"],
                "banlist": ["Uber Pokemon", "Arena Trap", "Moody", "Power Construct", "Shadow Tag", "Baton Pass"],
            },
            "UU": {
                "name": "UnderUsed",
                "level_cap": 100,
                "usage_threshold": 4.52,
                "clauses": ["Sleep Clause", "Species Clause", "OHKO Clause", "Evasion Clause", "Endless Battle Clause"],
                "banlist": ["OU Pokemon", "UUBL Pokemon", "Arena Trap", "Drizzle", "Drought"],
            },
        }
        return format_data.get(format.upper(), {"name": format, "description": "Custom format"})

    def _get_pokemon_pool(self, format: str) -> List[Dict[str, Any]]:
        """Get available Pokemon for the format with data."""
        try:
            with open(self.cache_dir.parent / "pokemon_roles.json", "r") as f:
                roles_data = json.load(f)
                return roles_data.get(format, [])
        except Exception:
            return []

    def _get_meta_context(self, format: str) -> Dict[str, Any]:
        """Get meta context data."""
        return {
            "common_cores": [
                {
                    "pokemon": ["Tyranitar", "Excadrill"],
                    "type": "Weather",
                    "synergy": "Sand Stream + Sand Rush",
                    "effectiveness": 85.2,
                },
                {
                    "pokemon": ["Pelipper", "Barraskewda"],
                    "type": "Weather",
                    "synergy": "Drizzle + Swift Swim",
                    "effectiveness": 82.8,
                },
            ],
            "popular_roles": {
                "physical_sweeper": 25.5,
                "special_sweeper": 22.3,
                "physical_wall": 15.8,
                "special_wall": 14.2,
                "mixed_attacker": 12.5,
                "support": 9.7,
            },
            "speed_control": {"trick_room": 15, "tailwind": 20, "priority": 30, "natural_speed": 35},
        }
