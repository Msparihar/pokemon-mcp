"""
Type effectiveness calculator for Pokemon battles.
"""

import json
from pathlib import Path
from typing import List, Dict, Union, Tuple


class TypeCalculator:
    """Handles type effectiveness calculations and type-related utilities."""

    def __init__(self):
        """Initialize with type effectiveness data."""
        self.type_chart = self._load_type_chart()

    def _load_type_chart(self) -> Dict:
        """Load type effectiveness data from JSON file."""
        try:
            data_path = Path(__file__).parent.parent / "data" / "type_effectiveness.json"
            with open(data_path, "r") as f:
                return json.load(f)
        except Exception as e:
            # Fallback to basic type chart if file not found
            return self._get_basic_type_chart()

    def _get_basic_type_chart(self) -> Dict:
        """Basic type chart fallback."""
        return {
            "type_chart": {
                "fire": {
                    "super_effective": ["grass", "ice", "bug", "steel"],
                    "not_very_effective": ["fire", "water", "rock", "dragon"],
                    "no_effect": [],
                },
                "water": {
                    "super_effective": ["fire", "ground", "rock"],
                    "not_very_effective": ["water", "grass", "dragon"],
                    "no_effect": [],
                },
            },
            "effectiveness_multipliers": {
                "super_effective": 2.0,
                "normal": 1.0,
                "not_very_effective": 0.5,
                "no_effect": 0.0,
            },
        }

    def get_effectiveness(self, attacking_type: str, defending_types: List[str]) -> float:
        """
        Calculate type effectiveness multiplier.

        Args:
            attacking_type: The attacking move's type
            defending_types: List of defending Pokemon's types (1 or 2 types)

        Returns:
            float: Effectiveness multiplier (0.0, 0.25, 0.5, 1.0, 2.0, or 4.0)
        """
        if attacking_type not in self.type_chart["type_chart"]:
            return 1.0

        effectiveness = 1.0
        attacking_data = self.type_chart["type_chart"][attacking_type]
        multipliers = self.type_chart["effectiveness_multipliers"]

        for defending_type in defending_types:
            if defending_type in attacking_data["super_effective"]:
                effectiveness *= multipliers["super_effective"]
            elif defending_type in attacking_data["not_very_effective"]:
                effectiveness *= multipliers["not_very_effective"]
            elif defending_type in attacking_data["no_effect"]:
                effectiveness *= multipliers["no_effect"]
            # else: normal effectiveness (1.0), no change needed

        return effectiveness

    def get_weaknesses(self, pokemon_types: List[str]) -> Dict[str, float]:
        """
        Get all type weaknesses for a Pokemon.

        Args:
            pokemon_types: List of Pokemon's types

        Returns:
            Dict mapping attacking types to effectiveness multipliers
        """
        weaknesses = {}

        for attacking_type in self.type_chart["type_chart"].keys():
            effectiveness = self.get_effectiveness(attacking_type, pokemon_types)
            if effectiveness > 1.0:
                weaknesses[attacking_type] = effectiveness

        return weaknesses

    def get_resistances(self, pokemon_types: List[str]) -> Dict[str, float]:
        """
        Get all type resistances for a Pokemon.

        Args:
            pokemon_types: List of Pokemon's types

        Returns:
            Dict mapping attacking types to effectiveness multipliers
        """
        resistances = {}

        for attacking_type in self.type_chart["type_chart"].keys():
            effectiveness = self.get_effectiveness(attacking_type, pokemon_types)
            if 0.0 < effectiveness < 1.0:
                resistances[attacking_type] = effectiveness

        return resistances

    def get_immunities(self, pokemon_types: List[str]) -> List[str]:
        """
        Get all type immunities for a Pokemon.

        Args:
            pokemon_types: List of Pokemon's types

        Returns:
            List of types the Pokemon is immune to
        """
        immunities = []

        for attacking_type in self.type_chart["type_chart"].keys():
            effectiveness = self.get_effectiveness(attacking_type, pokemon_types)
            if effectiveness == 0.0:
                immunities.append(attacking_type)

        return immunities

    def analyze_type_matchup(self, attacker_types: List[str], defender_types: List[str]) -> Dict:
        """
        Analyze type matchup between two Pokemon.

        Args:
            attacker_types: Attacking Pokemon's types
            defender_types: Defending Pokemon's types

        Returns:
            Dict with detailed matchup analysis
        """
        attacker_effectiveness = {}
        defender_effectiveness = {}

        # Calculate attacker's effectiveness against defender
        for attack_type in attacker_types:
            effectiveness = self.get_effectiveness(attack_type, defender_types)
            attacker_effectiveness[attack_type] = effectiveness

        # Calculate defender's effectiveness against attacker
        for defend_type in defender_types:
            effectiveness = self.get_effectiveness(defend_type, attacker_types)
            defender_effectiveness[defend_type] = effectiveness

        # Determine overall advantage
        max_attacker_eff = max(attacker_effectiveness.values())
        max_defender_eff = max(defender_effectiveness.values())

        if max_attacker_eff > max_defender_eff:
            advantage = "attacker"
        elif max_defender_eff > max_attacker_eff:
            advantage = "defender"
        else:
            advantage = "neutral"

        return {
            "attacker_effectiveness": attacker_effectiveness,
            "defender_effectiveness": defender_effectiveness,
            "advantage": advantage,
            "attacker_best_multiplier": max_attacker_eff,
            "defender_best_multiplier": max_defender_eff,
        }

    def get_offensive_coverage(self, team_types: List[List[str]]) -> Dict:
        """
        Analyze offensive type coverage for a team.

        Args:
            team_types: List of type lists for each team member

        Returns:
            Dict with coverage analysis
        """
        all_types = list(self.type_chart["type_chart"].keys())
        coverage = {}

        for target_type in all_types:
            best_effectiveness = 0.0
            covering_types = []

            for pokemon_types in team_types:
                for move_type in pokemon_types:
                    effectiveness = self.get_effectiveness(move_type, [target_type])
                    if effectiveness > best_effectiveness:
                        best_effectiveness = effectiveness
                        covering_types = [move_type]
                    elif effectiveness == best_effectiveness and effectiveness > 1.0:
                        covering_types.append(move_type)

            coverage[target_type] = {"effectiveness": best_effectiveness, "covering_types": list(set(covering_types))}

        super_effective_count = sum(1 for c in coverage.values() if c["effectiveness"] >= 2.0)
        coverage_score = super_effective_count / len(all_types)

        return {
            "individual_coverage": coverage,
            "super_effective_against": super_effective_count,
            "total_types": len(all_types),
            "coverage_score": coverage_score,
        }
