"""
Pokemon search and filtering engine.
"""

import re
from typing import Dict, List, Optional, Any
from modules.role_classifier import RoleClassifier
from utils.type_calculator import TypeCalculator


class SearchEngine:
    """Advanced Pokemon search with multiple filtering capabilities."""

    def __init__(self, pokemon_data_fetcher):
        """
        Initialize search engine.

        Args:
            pokemon_data_fetcher: Function to fetch Pokemon data from API
        """
        self.fetch_pokemon = pokemon_data_fetcher
        self.role_classifier = RoleClassifier()
        self.type_calculator = TypeCalculator()
        self._pokemon_cache = {}

    def search_pokemon(
        self,
        query: str = None,
        type_filter: str = None,
        role_filter: str = None,
        stat_range: Dict[str, int] = None,
        limit: int = 10,
    ) -> Dict[str, Any]:
        """
        Advanced Pokemon search with multiple filters.

        Args:
            query: Pokemon name or partial name
            type_filter: Single type filter
            role_filter: Pokemon role filter
            stat_range: Minimum stat requirements
            limit: Maximum number of results

        Returns:
            Dict with search results and metadata
        """
        try:
            # Get initial Pokemon list
            if query:
                pokemon_list = self._search_by_name(query)
            else:
                # For now, get a sample of popular Pokemon if no query
                pokemon_list = self._get_sample_pokemon()

            # Apply filters
            filtered_results = self._apply_filters(pokemon_list, type_filter, role_filter, stat_range)

            # Sort and limit results
            sorted_results = self._sort_results(filtered_results, role_filter)
            limited_results = sorted_results[:limit]

            # Enrich results with additional data
            enriched_results = self._enrich_results(limited_results)

            return {
                "results": enriched_results,
                "count": len(limited_results),
                "total_found": len(sorted_results),
                "filters_applied": {
                    "query": query,
                    "type_filter": type_filter,
                    "role_filter": role_filter,
                    "stat_range": stat_range,
                    "limit": limit,
                },
                "suggestions": self._generate_suggestions(len(sorted_results), limit, role_filter, type_filter),
            }

        except Exception as e:
            return {
                "results": [],
                "count": 0,
                "total_found": 0,
                "error": f"Search failed: {str(e)}",
                "filters_applied": {},
                "suggestions": [],
            }

    def _search_by_name(self, query: str) -> List[Dict]:
        """Search Pokemon by name or partial name."""
        query = query.lower().strip()
        results = []

        # Try exact match first
        try:
            pokemon_data = self.fetch_pokemon(query)
            if pokemon_data:
                results.append(pokemon_data)
        except:
            pass

        # If no exact match and query is partial, try common Pokemon
        if not results and len(query) >= 3:
            common_pokemon = self._get_pokemon_by_partial_name(query)
            results.extend(common_pokemon)

        return results

    def _get_pokemon_by_partial_name(self, partial: str) -> List[Dict]:
        """Get Pokemon that match partial name."""
        # This is a simplified implementation
        # In a full implementation, you'd have a Pokemon name database
        common_matches = {
            "char": ["charizard", "charmander", "charmeleon"],
            "pika": ["pikachu", "pichu"],
            "blast": ["blastoise"],
            "venu": ["venusaur"],
            "squ": ["squirtle", "wartortle"],
            "bulb": ["bulbasaur", "ivysaur"],
            "garcho": ["garchomp"],
            "drago": ["dragonite", "dragapult"],
            "meta": ["metagross", "metang"],
            "sal": ["salamence"],
            "ttar": ["tyranitar"],
            "skarm": ["skarmory"],
            "blis": ["blissey"],
            "rotom": ["rotom"],
            "ferro": ["ferrothorn"],
            "sciz": ["scizor"],
            "mamo": ["mamoswine"],
            "lando": ["landorus"],
            "heat": ["heatran"],
        }

        results = []
        for key, pokemon_names in common_matches.items():
            if partial in key:
                for name in pokemon_names:
                    try:
                        pokemon_data = self.fetch_pokemon(name)
                        if pokemon_data:
                            results.append(pokemon_data)
                    except:
                        continue

        return results

    def _get_sample_pokemon(self) -> List[Dict]:
        """Get a sample of popular Pokemon for general searches."""
        sample_names = [
            "charizard",
            "blastoise",
            "venusaur",
            "pikachu",
            "garchomp",
            "dragonite",
            "metagross",
            "salamence",
            "tyranitar",
            "alakazam",
            "gengar",
            "machamp",
            "golem",
            "arcanine",
            "gyarados",
            "lapras",
            "snorlax",
            "umbreon",
            "espeon",
            "scizor",
            "skarmory",
            "blissey",
            "swampert",
            "blaziken",
            "gardevoir",
            "aggron",
            "flygon",
            "lucario",
            "garchomp",
            "dialga",
        ]

        results = []
        for name in sample_names[:20]:  # Limit to prevent API overload
            try:
                pokemon_data = self.fetch_pokemon(name)
                if pokemon_data:
                    results.append(pokemon_data)
            except:
                continue

        return results

    def _apply_filters(
        self,
        pokemon_list: List[Dict],
        type_filter: str = None,
        role_filter: str = None,
        stat_range: Dict[str, int] = None,
    ) -> List[Dict]:
        """Apply various filters to Pokemon list."""
        filtered = pokemon_list.copy()

        # Type filter
        if type_filter:
            filtered = [p for p in filtered if self._has_type(p, type_filter.lower())]

        # Stat range filter
        if stat_range:
            filtered = [p for p in filtered if self._meets_stat_requirements(p, stat_range)]

        # Role filter
        if role_filter:
            filtered = self._filter_by_role(filtered, role_filter)

        return filtered

    def _has_type(self, pokemon: Dict, type_name: str) -> bool:
        """Check if Pokemon has the specified type."""
        types = pokemon.get("types", [])
        pokemon_type_names = []

        for type_info in types:
            if isinstance(type_info, dict):
                type_name_data = type_info.get("type", {}).get("name", "")
                pokemon_type_names.append(type_name_data.lower())
            elif isinstance(type_info, str):
                pokemon_type_names.append(type_info.lower())

        return type_name in pokemon_type_names

    def _meets_stat_requirements(self, pokemon: Dict, stat_range: Dict[str, int]) -> bool:
        """Check if Pokemon meets stat requirements."""
        stats = pokemon.get("stats", [])

        # Convert stats array to dict if needed
        if isinstance(stats, list):
            stat_dict = {}
            for stat in stats:
                if isinstance(stat, dict):
                    stat_name = stat.get("stat", {}).get("name", "")
                    stat_value = stat.get("base_stat", 0)
                    stat_dict[stat_name] = stat_value
        else:
            stat_dict = stats

        # Check each requirement
        for stat_name, min_value in stat_range.items():
            # Handle different stat name formats
            actual_value = (
                stat_dict.get(stat_name, 0)
                or stat_dict.get(stat_name.replace("_", "-"), 0)
                or stat_dict.get(stat_name.replace("-", "_"), 0)
            )

            if actual_value < min_value:
                return False

        return True

    def _filter_by_role(self, pokemon_list: List[Dict], role_filter: str) -> List[Dict]:
        """Filter Pokemon by role classification."""
        filtered_pokemon = []

        for pokemon in pokemon_list:
            classification = self.role_classifier.classify_pokemon(pokemon)

            # Check if Pokemon fits the role
            if classification["primary_role"] == role_filter or role_filter in classification["qualifying_roles"]:
                # Add role info to Pokemon data
                pokemon_with_role = pokemon.copy()
                pokemon_with_role["role_info"] = classification
                filtered_pokemon.append(pokemon_with_role)

        return filtered_pokemon

    def _sort_results(self, pokemon_list: List[Dict], role_filter: str = None) -> List[Dict]:
        """Sort search results by relevance."""

        def sort_key(pokemon):
            # Base score
            score = 0.0

            # If role filtering, prioritize role score
            if role_filter and "role_info" in pokemon:
                score += pokemon["role_info"]["role_score"] * 100

            # Prioritize by base stat total
            stats = pokemon.get("stats", [])
            if isinstance(stats, list):
                total_stats = sum(stat.get("base_stat", 0) for stat in stats if isinstance(stat, dict))
            else:
                total_stats = sum(stats.values()) if stats else 0

            score += total_stats / 10  # Normalize to 0-60 range

            # Small bonus for popular Pokemon (those with lower IDs)
            pokemon_id = pokemon.get("id", 1000)
            if pokemon_id <= 151:  # Gen 1
                score += 20
            elif pokemon_id <= 251:  # Gen 2
                score += 15
            elif pokemon_id <= 386:  # Gen 3
                score += 10

            return score

        return sorted(pokemon_list, key=sort_key, reverse=True)

    def _enrich_results(self, pokemon_list: List[Dict]) -> List[Dict]:
        """Enrich results with additional computed data."""
        enriched = []

        for pokemon in pokemon_list:
            enriched_pokemon = pokemon.copy()

            # Add role classification if not present
            if "role_info" not in enriched_pokemon:
                classification = self.role_classifier.classify_pokemon(pokemon)
                enriched_pokemon["role_info"] = classification

            # Add type effectiveness summary
            types = self._extract_types(pokemon)
            if types:
                enriched_pokemon["type_analysis"] = {
                    "weaknesses": self.type_calculator.get_weaknesses(types),
                    "resistances": self.type_calculator.get_resistances(types),
                    "immunities": self.type_calculator.get_immunities(types),
                }

            # Add formatted data for easy access
            enriched_pokemon["formatted"] = self._format_pokemon_data(pokemon)

            enriched.append(enriched_pokemon)

        return enriched

    def _extract_types(self, pokemon: Dict) -> List[str]:
        """Extract type names from Pokemon data."""
        types = pokemon.get("types", [])
        type_names = []

        for type_info in types:
            if isinstance(type_info, dict):
                type_name = type_info.get("type", {}).get("name", "")
                if type_name:
                    type_names.append(type_name.lower())
            elif isinstance(type_info, str):
                type_names.append(type_info.lower())

        return type_names

    def _format_pokemon_data(self, pokemon: Dict) -> Dict:
        """Format Pokemon data for consistent access."""
        # Extract basic info
        name = pokemon.get("name", "unknown")
        pokemon_id = pokemon.get("id", 0)
        types = self._extract_types(pokemon)

        # Extract and normalize stats
        stats = pokemon.get("stats", [])
        if isinstance(stats, list):
            stat_dict = {}
            for stat in stats:
                if isinstance(stat, dict):
                    stat_name = stat.get("stat", {}).get("name", "")
                    stat_value = stat.get("base_stat", 0)
                    # Normalize stat names
                    normalized_name = stat_name.replace("-", "_")
                    stat_dict[normalized_name] = stat_value
        else:
            stat_dict = stats

        # Extract abilities
        abilities = []
        ability_data = pokemon.get("abilities", [])
        for ability in ability_data:
            if isinstance(ability, dict):
                ability_name = ability.get("ability", {}).get("name", "")
                if ability_name:
                    abilities.append(ability_name)

        return {
            "name": name,
            "id": pokemon_id,
            "types": types,
            "stats": stat_dict,
            "abilities": abilities,
            "total_stats": sum(stat_dict.values()) if stat_dict else 0,
        }

    def _generate_suggestions(
        self, total_found: int, limit: int, role_filter: str = None, type_filter: str = None
    ) -> List[str]:
        """Generate helpful suggestions for improving search results."""
        suggestions = []

        if total_found == 0:
            suggestions.append("No Pokemon found matching your criteria")
            if role_filter:
                suggestions.append(f"Try a different role instead of '{role_filter}'")
            if type_filter:
                suggestions.append(f"Try a different type instead of '{type_filter}'")
            suggestions.append("Try removing some filters to see more results")

        elif total_found > limit:
            suggestions.append(f"Showing {limit} of {total_found} results")
            if not role_filter:
                suggestions.append("Add a role filter to narrow down results")
            if not type_filter:
                suggestions.append("Add a type filter to find more specific Pokemon")

        elif total_found < 5:
            suggestions.append("Try removing some filters for more results")

        return suggestions

    def get_pokemon_by_criteria(self, criteria: Dict[str, Any]) -> List[Dict]:
        """
        Get Pokemon matching specific criteria.

        Args:
            criteria: Dict with search criteria

        Returns:
            List of matching Pokemon
        """
        return self.search_pokemon(
            query=criteria.get("query"),
            type_filter=criteria.get("type"),
            role_filter=criteria.get("role"),
            stat_range=criteria.get("stats"),
            limit=criteria.get("limit", 50),
        )["results"]
