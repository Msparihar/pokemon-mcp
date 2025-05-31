"""
Pokemon role classification system.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class RoleClassifier:
    """Classifies Pokemon into competitive roles based on stats and characteristics."""

    def __init__(self):
        """Initialize with role definitions."""
        self.role_data = self._load_role_data()

    def _load_role_data(self) -> Dict:
        """Load role definitions from JSON file."""
        try:
            data_path = Path(__file__).parent.parent / "data" / "pokemon_roles.json"
            with open(data_path, "r") as f:
                return json.load(f)
        except Exception as e:
            # Fallback to basic role definitions
            return self._get_basic_roles()

    def _get_basic_roles(self) -> Dict:
        """Basic role definitions fallback."""
        return {
            "role_definitions": {
                "physical_wall": {"stat_requirements": {"defense": 90, "hp": 60}, "preferred_stats": ["defense", "hp"]},
                "special_wall": {
                    "stat_requirements": {"sp_defense": 90, "hp": 60},
                    "preferred_stats": ["sp_defense", "hp"],
                },
                "physical_sweeper": {
                    "stat_requirements": {"attack": 100, "speed": 80},
                    "preferred_stats": ["attack", "speed"],
                },
                "special_sweeper": {
                    "stat_requirements": {"sp_attack": 100, "speed": 80},
                    "preferred_stats": ["sp_attack", "speed"],
                },
            }
        }

    def classify_pokemon(self, pokemon_data: Dict) -> Dict:
        """
        Classify a Pokemon into roles based on its stats.

        Args:
            pokemon_data: Dict containing Pokemon stats

        Returns:
            Dict with role classification results
        """
        stats = pokemon_data.get("stats", {})

        # Convert stat names to match our requirements
        normalized_stats = {
            "hp": stats.get("hp", 0),
            "attack": stats.get("attack", 0),
            "defense": stats.get("defense", 0),
            "sp_attack": stats.get("special-attack", stats.get("sp_attack", 0)),
            "sp_defense": stats.get("special-defense", stats.get("sp_defense", 0)),
            "speed": stats.get("speed", 0),
        }

        role_scores = {}
        qualifying_roles = []

        for role_name, role_def in self.role_data["role_definitions"].items():
            score = self._calculate_role_score(normalized_stats, role_def)
            role_scores[role_name] = score

            # Check if Pokemon meets minimum requirements
            if self._meets_requirements(normalized_stats, role_def["stat_requirements"]):
                qualifying_roles.append(role_name)

        # Determine primary role (highest score among qualifying roles)
        if qualifying_roles:
            primary_role = max(qualifying_roles, key=lambda r: role_scores[r])
        else:
            # If no role requirements met, choose highest scoring role
            primary_role = max(role_scores, key=role_scores.get)

        # Calculate overall role effectiveness
        role_effectiveness = role_scores[primary_role]

        return {
            "primary_role": primary_role,
            "role_score": role_effectiveness,
            "all_role_scores": role_scores,
            "qualifying_roles": qualifying_roles,
            "role_description": self.role_data["role_definitions"][primary_role].get("description", ""),
            "stat_analysis": self._analyze_stats(normalized_stats),
        }

    def _calculate_role_score(self, stats: Dict, role_def: Dict) -> float:
        """Calculate how well a Pokemon fits a specific role."""
        requirements = role_def["stat_requirements"]
        preferred_stats = role_def.get("preferred_stats", [])

        # Base score from meeting requirements
        requirement_score = 0.0
        total_requirements = len(requirements)

        for stat, min_value in requirements.items():
            if stats.get(stat, 0) >= min_value:
                # Bonus for exceeding requirements
                excess = stats[stat] - min_value
                requirement_score += 1.0 + min(excess / 50.0, 0.5)  # Up to 0.5 bonus
            else:
                # Penalty for not meeting requirements
                deficit = min_value - stats.get(stat, 0)
                requirement_score += max(0.0, 1.0 - deficit / 30.0)  # Scaled penalty

        # Average requirement score
        base_score = requirement_score / total_requirements if total_requirements > 0 else 0.0

        # Bonus for having high preferred stats
        preferred_bonus = 0.0
        if preferred_stats:
            preferred_total = sum(stats.get(stat, 0) for stat in preferred_stats)
            # Normalize based on typical stat totals (around 500-600)
            preferred_bonus = min(preferred_total / 300.0, 0.3)  # Up to 0.3 bonus

        final_score = min(base_score + preferred_bonus, 1.0)
        return round(final_score, 3)

    def _meets_requirements(self, stats: Dict, requirements: Dict) -> bool:
        """Check if Pokemon meets minimum stat requirements for a role."""
        for stat, min_value in requirements.items():
            if stats.get(stat, 0) < min_value:
                return False
        return True

    def _analyze_stats(self, stats: Dict) -> Dict:
        """Analyze Pokemon's stat distribution."""
        total_stats = sum(stats.values())

        # Identify stat specializations
        highest_stat = max(stats, key=stats.get)
        lowest_stat = min(stats, key=stats.get)

        # Calculate stat ratios
        offensive_ratio = (stats["attack"] + stats["sp_attack"]) / total_stats if total_stats > 0 else 0
        defensive_ratio = (stats["defense"] + stats["sp_defense"] + stats["hp"]) / total_stats if total_stats > 0 else 0
        speed_ratio = stats["speed"] / total_stats if total_stats > 0 else 0

        # Determine stat focus
        if offensive_ratio > 0.4:
            stat_focus = "offensive"
        elif defensive_ratio > 0.6:
            stat_focus = "defensive"
        elif speed_ratio > 0.2:
            stat_focus = "speed"
        else:
            stat_focus = "balanced"

        return {
            "total_stats": total_stats,
            "highest_stat": highest_stat,
            "lowest_stat": lowest_stat,
            "offensive_ratio": round(offensive_ratio, 3),
            "defensive_ratio": round(defensive_ratio, 3),
            "speed_ratio": round(speed_ratio, 3),
            "stat_focus": stat_focus,
        }

    def get_role_recommendations(self, pokemon_data: Dict) -> List[Dict]:
        """
        Get role recommendations with explanations.

        Args:
            pokemon_data: Dict containing Pokemon data

        Returns:
            List of role recommendations with reasoning
        """
        classification = self.classify_pokemon(pokemon_data)
        role_scores = classification["all_role_scores"]

        # Sort roles by score
        sorted_roles = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)

        recommendations = []
        for role_name, score in sorted_roles[:3]:  # Top 3 recommendations
            role_def = self.role_data["role_definitions"][role_name]

            # Generate explanation
            explanation = self._generate_role_explanation(pokemon_data, role_name, role_def, score)

            recommendations.append(
                {
                    "role": role_name,
                    "score": score,
                    "description": role_def.get("description", ""),
                    "explanation": explanation,
                    "viability": self._get_viability_rating(score),
                }
            )

        return recommendations

    def _generate_role_explanation(self, pokemon_data: Dict, role_name: str, role_def: Dict, score: float) -> str:
        """Generate explanation for why a Pokemon fits (or doesn't fit) a role."""
        stats = pokemon_data.get("stats", {})
        requirements = role_def["stat_requirements"]

        explanations = []

        for stat, min_value in requirements.items():
            actual_value = stats.get(stat.replace("_", "-"), stats.get(stat, 0))
            if actual_value >= min_value:
                if actual_value >= min_value * 1.2:
                    explanations.append(f"Excellent {stat.replace('_', ' ')} ({actual_value})")
                else:
                    explanations.append(f"Good {stat.replace('_', ' ')} ({actual_value})")
            else:
                explanations.append(f"Low {stat.replace('_', ' ')} ({actual_value}, needs {min_value})")

        return "; ".join(explanations)

    def _get_viability_rating(self, score: float) -> str:
        """Convert numerical score to viability rating."""
        if score >= 0.8:
            return "Excellent"
        elif score >= 0.6:
            return "Good"
        elif score >= 0.4:
            return "Fair"
        else:
            return "Poor"

    def get_pokemon_by_role(self, role: str, pokemon_list: List[Dict]) -> List[Dict]:
        """
        Filter Pokemon list by role classification.

        Args:
            role: Role name to filter by
            pokemon_list: List of Pokemon data dicts

        Returns:
            List of Pokemon that fit the specified role
        """
        matching_pokemon = []

        for pokemon in pokemon_list:
            classification = self.classify_pokemon(pokemon)

            if classification["primary_role"] == role or role in classification["qualifying_roles"]:
                pokemon_with_role = pokemon.copy()
                pokemon_with_role["role_info"] = classification
                matching_pokemon.append(pokemon_with_role)

        # Sort by role score (best fits first)
        matching_pokemon.sort(key=lambda p: p["role_info"]["role_score"], reverse=True)

        return matching_pokemon
