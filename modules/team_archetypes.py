"""
Team archetypes module that provides data for Pokemon team building strategies.
"""

import requests
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from utils.type_calculator import TypeCalculator


class TeamArchetypes:
    """Provides data for team building archetypes and strategies."""

    def __init__(self):
        """Initialize with required components."""
        self.type_calculator = TypeCalculator()
        self.pokeapi_base = "https://pokeapi.co/api/v2"
        self.cache_dir = Path(__file__).parent.parent / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_team_suggestion(
        self, archetype: str, format: str = "OU", key_pokemon: Optional[str] = None, style: str = "balanced"
    ) -> Dict[str, Any]:
        """Provide data for team archetype suggestions."""
        try:
            # Validate archetype
            if not self._is_valid_archetype(archetype):
                return {"error": f"Invalid archetype: {archetype}"}

            # Get archetype requirements
            requirements = self._get_archetype_requirements(archetype)

            # Get core members data
            core_members = self._get_core_pokemon_data(archetype, key_pokemon)
            if not core_members:
                return {"error": "Failed to get core member data"}

            # Get team type data
            team_types = [member["types"] for member in core_members]
            type_data = self.type_calculator.get_team_type_data(team_types)

            return {
                "archetype": archetype,
                "format_info": self._get_format_data(format),
                "core_pokemon": core_members,
                "type_data": type_data,
                "requirements": requirements,
                "style_context": self._get_style_data(style),
                "archetype_data": self._get_archetype_data(archetype),
                "meta_context": self._get_meta_context(format),
            }

        except Exception as e:
            return {"error": f"Team suggestion failed: {str(e)}", "archetype": archetype}

    def _is_valid_archetype(self, archetype: str) -> bool:
        """Check if archetype is valid."""
        valid_archetypes = {
            "rain",
            "sun",
            "sand",
            "hail",  # Weather teams
            "trick_room",
            "tailwind",  # Speed control
            "hyper_offense",
            "stall",  # Play styles
            "volt_turn",
            "dragon_spam",  # Specific strategies
        }
        return archetype.lower() in valid_archetypes

    def _get_archetype_requirements(self, archetype: str) -> Dict[str, Any]:
        """Get archetype-specific requirements."""
        requirements = {
            "rain": {
                "core_roles": ["Weather Setter", "Swift Swim Sweeper"],
                "key_abilities": ["Drizzle", "Swift Swim", "Rain Dish"],
                "recommended_moves": ["Rain Dance", "Thunder", "Weather Ball", "Hurricane"],
                "key_pokemon": ["Pelipper", "Barraskewda", "Swampert"],
            },
            "trick_room": {
                "core_roles": ["TR Setter", "Slow Sweeper"],
                "key_abilities": ["Levitate", "Terrify", "Magic Guard"],
                "recommended_moves": ["Trick Room", "Gyro Ball", "Body Press"],
                "key_pokemon": ["Dusclops", "Glastrier", "Conkeldurr"],
            },
        }
        return requirements.get(archetype, {})

    def _get_core_pokemon_data(self, archetype: str, key_pokemon: Optional[str]) -> List[Dict[str, Any]]:
        """Get data for core team members."""
        core_members = []

        # Add key Pokemon if provided
        if key_pokemon:
            data = self.fetch_pokemon_data(key_pokemon)
            if "error" not in data:
                core_members.append(data)

        # Add archetype-specific Pokemon
        requirements = self._get_archetype_requirements(archetype)
        for pokemon in requirements.get("key_pokemon", [])[:2]:  # Get first two key Pokemon
            if pokemon.lower() != key_pokemon:
                data = self.fetch_pokemon_data(pokemon)
                if "error" not in data:
                    core_members.append(data)

        return core_members

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
                "abilities": [{"name": a["ability"]["name"], "is_hidden": a["is_hidden"]} for a in data["abilities"]],
                "moves": [m["move"]["name"] for m in data["moves"]],
            }

            with open(cache_file, "w") as f:
                json.dump(pokemon_data, f, indent=2)

            return pokemon_data

        except Exception as e:
            return {"error": f"Failed to fetch data for {name}: {str(e)}"}

    def _get_format_data(self, format: str) -> Dict[str, Any]:
        """Get format-specific data."""
        return {
            "name": format.upper(),
            "level_cap": 100,
            "allowed_pokemon": self._get_format_pokemon(format),
            "common_archetypes": self._get_common_archetypes(format),
        }

    def _get_style_data(self, style: str) -> Dict[str, Any]:
        """Get style-specific data."""
        styles = {
            "balanced": {
                "offensive_weight": 0.5,
                "defensive_weight": 0.5,
                "recommended_roles": ["Sweeper", "Wall", "Support", "Breaker"],
            },
            "offensive": {
                "offensive_weight": 0.8,
                "defensive_weight": 0.2,
                "recommended_roles": ["Sweeper", "Wallbreaker", "Cleaner"],
            },
            "defensive": {
                "offensive_weight": 0.2,
                "defensive_weight": 0.8,
                "recommended_roles": ["Wall", "Support", "Pivot"],
            },
        }
        return styles.get(style, styles["balanced"])

    def _get_archetype_data(self, archetype: str) -> Dict[str, Any]:
        """Get detailed archetype data."""
        return {
            "playstyle": {
                "rain": "Offensive weather team focusing on water-type moves and Swift Swim",
                "trick_room": "Speed control team focusing on slow but powerful Pokemon",
            }.get(archetype, "Custom strategy"),
            "common_cores": self._get_archetype_cores(archetype),
            "common_roles": self._get_archetype_roles(archetype),
            "synergy_requirements": self._get_synergy_requirements(archetype),
        }

    def _get_meta_context(self, format: str) -> Dict[str, Any]:
        """Get meta context data."""
        return {
            "common_threats": [
                {"pokemon": "Dragapult", "usage": 25.5, "threat_level": "high"},
                {"pokemon": "Heatran", "usage": 20.1, "threat_level": "high"},
            ],
            "popular_play_styles": {"hyper_offense": 35, "balance": 40, "stall": 25},
            "common_support": ["Defog", "Stealth Rock", "Wish", "Volt Switch"],
        }

    def _get_format_pokemon(self, format: str) -> List[Dict[str, Any]]:
        """Get format-legal Pokemon data."""
        try:
            with open(self.cache_dir.parent / "pokemon_roles.json", "r") as f:
                roles_data = json.load(f)
                return roles_data.get(format, [])
        except Exception:
            return []

    def _get_common_archetypes(self, format: str) -> List[Dict[str, Any]]:
        """Get common archetypes in the format."""
        return [
            {"name": "Rain", "usage": 15.5, "success_rate": 52.3, "core_pokemon": ["Pelipper", "Barraskewda"]},
            {"name": "Sand", "usage": 12.8, "success_rate": 51.8, "core_pokemon": ["Tyranitar", "Excadrill"]},
        ]

    def _get_archetype_cores(self, archetype: str) -> List[Dict[str, Any]]:
        """Get common cores for the archetype."""
        cores = {
            "rain": [
                {"pokemon": ["Pelipper", "Barraskewda"], "synergy": "Weather + Swift Swim", "effectiveness": 85.2}
            ],
            "trick_room": [
                {"pokemon": ["Dusclops", "Glastrier"], "synergy": "TR Setter + Sweeper", "effectiveness": 82.8}
            ],
        }
        return cores.get(archetype, [])

    def _get_archetype_roles(self, archetype: str) -> List[str]:
        """Get required roles for the archetype."""
        roles = {
            "rain": ["Weather Setter", "Swift Swim Sweeper", "Thunder User"],
            "trick_room": ["TR Setter", "Slow Sweeper", "Redirection"],
        }
        return roles.get(archetype, [])

    def _get_synergy_requirements(self, archetype: str) -> Dict[str, Any]:
        """Get synergy requirements for the archetype."""
        requirements = {
            "rain": {
                "abilities": ["Drizzle", "Swift Swim"],
                "moves": ["Thunder", "Hurricane"],
                "coverage": ["Electric", "Flying"],
            },
            "trick_room": {
                "abilities": ["Levitate", "Terrify"],
                "moves": ["Trick Room", "Imprison"],
                "coverage": ["Fighting", "Ghost"],
            },
        }
        return requirements.get(archetype, {})
