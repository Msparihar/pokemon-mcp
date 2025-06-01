"""
Type data provider for Pokemon types and relationships.
"""

import json
import requests
from pathlib import Path
from typing import List, Dict, Any


class TypeCalculator:
    """Provides Pokemon type data and relationships."""

    def __init__(self):
        """Initialize with type data sources."""
        self.pokeapi_base = "https://pokeapi.co/api/v2"
        self.cache_dir = Path(__file__).parent.parent / "data" / "cache"
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.type_data = self._load_type_data()

    def _load_type_data(self) -> Dict[str, Any]:
        """Load type data from cache or fetch from PokeAPI."""
        cache_file = self.cache_dir / "type_data.json"

        if cache_file.exists():
            with open(cache_file, "r") as f:
                return json.load(f)

        try:
            # Fetch all type data from PokeAPI
            response = requests.get(f"{self.pokeapi_base}/type")
            types = response.json()["results"]
            type_data = {}

            for type_info in types:
                type_response = requests.get(type_info["url"])
                type_data[type_info["name"]] = type_response.json()

            # Cache the data
            with open(cache_file, "w") as f:
                json.dump(type_data, f, indent=2)

            return type_data

        except Exception as e:
            return self._get_basic_type_data()

    def _get_basic_type_data(self) -> Dict[str, Any]:
        """Fallback type data if API fails."""
        try:
            data_path = Path(__file__).parent.parent / "data" / "type_effectiveness.json"
            with open(data_path, "r") as f:
                return json.load(f)
        except Exception:
            return {}

    def get_effectiveness(self, attacking_type: str, defending_types: List[str]) -> Dict[str, Any]:
        """Get raw type effectiveness data."""
        return {
            "attacking_type": attacking_type.lower(),
            "attacking_type_data": self.type_data.get(attacking_type.lower(), {}),
            "defending_types": [t.lower() for t in defending_types],
            "defending_types_data": {t.lower(): self.type_data.get(t.lower(), {}) for t in defending_types},
            "all_type_relations": self.type_data,
        }

    def get_team_type_data(self, team_types: List[List[str]]) -> Dict[str, Any]:
        """Get comprehensive type data for a team."""
        return {
            "team_types": team_types,
            "type_data": {
                str(types): {t.lower(): self.type_data.get(t.lower(), {}) for t in types} for types in team_types
            },
            "all_type_relations": self.type_data,
        }

    def analyze_team_types(self, team1_types: List[List[str]], team2_types: List[List[str]]) -> Dict[str, Any]:
        """Get type data for team matchup analysis."""
        return {
            "team1_types": team1_types,
            "team1_data": {
                str(types): {t.lower(): self.type_data.get(t.lower(), {}) for t in types} for types in team1_types
            },
            "team2_types": team2_types,
            "team2_data": {
                str(types): {t.lower(): self.type_data.get(t.lower(), {}) for t in types} for types in team2_types
            },
            "all_type_relations": self.type_data,
        }

    def get_pokemon_type_data(self, pokemon_types: List[str]) -> Dict[str, Any]:
        """Get all type data for a Pokemon."""
        return {
            "pokemon_types": pokemon_types,
            "type_data": {t.lower(): self.type_data.get(t.lower(), {}) for t in pokemon_types},
            "all_type_relations": self.type_data,
        }
