from experta import KnowledgeEngine
from typing import Dict, Optional

class SolarSystemExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.possible_planets = {
            'Mercury': 1.0 / 8, 'Venus': 1.0 / 8, 'Earth': 1.0 / 8, 'Mars': 1.0 / 8,
            'Jupiter': 1.0 / 8, 'Saturn': 1.0 / 8, 'Uranus': 1.0 / 8, 'Neptune': 1.0 / 8
        }
        self.questions = [
            ("is_gas_giant", "Is it a gas giant?", {
                'Jupiter': True,
                'Saturn': True,
                'Uranus': True,
                'Neptune': True,
                'Mercury': False,
                'Venus': False,
                'Earth': False,
                'Mars': False
            }),
            ("has_rings", "Does it have prominent rings?", {
                'Jupiter': True,
                'Saturn': True,
                'Uranus': False,  # Uranus has faint rings but not prominent
                'Neptune': False,  # Neptune has faint rings but not prominent
                'Mercury': False,
                'Venus': False,
                'Earth': False,
                'Mars': False
            }),
            ("is_inner_planet", "Is it one of the inner planets (closer to the Sun)?", {
                'Mercury': True,
                'Venus': True,
                'Earth': True,
                'Mars': True,
                'Jupiter': False,
                'Saturn': False,
                'Uranus': False,
                'Neptune': False
            }),
            ("has_atmosphere", "Does it have a substantial atmosphere?", {
                'Venus': True,
                'Earth': True,
                'Jupiter': True,
                'Saturn': True,
                'Uranus': True,
                'Neptune': True,
                'Mars': False,
                'Mercury': False
            }),
            ("is_habitable", "Is it potentially habitable or known to harbor life?", {
                'Earth': True,
                'Mercury': False,
                'Venus': False,
                'Mars': False,  # Mars has potential for past life but is not currently habitable
                'Jupiter': False,
                'Saturn': False,
                'Uranus': False,
                'Neptune': False
            }),
            ("extreme_temp", "Is it known for extreme temperatures?", {
                'Mercury': True,  # Known for extreme temperature fluctuations
                'Venus': True,     # Extremely high temperatures
                'Earth': False,    # Moderate temperatures
                'Mars': True,      # Cold temperatures but not extreme like Venus or Mercury
                'Jupiter': True,   # Known for storms and extreme conditions
                'Saturn': False,   # Not particularly extreme compared to others
                'Uranus': False,   # Has cold temperatures but not extreme in the same sense
                'Neptune': False    # Similar to Uranus in terms of coldness
            }),
            ("has_moons", "Does it have significant moons?", {
                # Correcting the moon information
                'Earth': True,     # Has 1 significant moon
                'Mars': True,      # Has 2 small moons (Phobos and Deimos)
                'Jupiter': True,   # Has many moons (over 79)
                'Saturn': True,    # Also has many moons (over 80)
                'Uranus': True,    # Has 27 known moons
                'Neptune': True,   # Has 14 known moons
                'Mercury': False,  # No moons
                'Venus': False      # No moons
            }),
            ("color", "Is it predominantly blue?", {
            # Only Uranus and Neptune are predominantly blue.
            # Jupiter and Saturn are not predominantly blue; Earth is not predominantly blue.
            # Mercury and Venus are also not blue.
            'Jupiter': False,
            'Saturn': False,
            'Uranus': True,   # Predominantly blue due to methane in the atmosphere
            'Neptune': True,   # Also appears blue for similar reasons
            # Inner planets are not blue
            'Mercury': False,
            'Venus': False,
            'Earth': False,     # Earth is often depicted as blue due to oceans but not predominantly so in this context.
            'Mars': False       # Mars is red.
            }),
            ("has_retrograde_moon", "Does it have a retrograde moon?", {
            # Triton is the only large retrograde moon in the solar system.
            # This question helps distinguish Neptune from Uranus.
            "Jupiter": False,   # No retrograde large moons.
            "Saturn": False,    # No retrograde large moons.
            "Uranus": False,    # No significant retrograde moons.
            "Neptune": True,    # Triton is a retrograde moon.
            "Mercury": False,   # No moons.
            "Venus": False,     # No moons.
            "Earth": False,     # Moon is not retrograde.
            "Mars": False       # Moons are not retrograde.
            })
        ]
        self.asked_questions = set()
        self.question_count = 0 
    def update_probabilities(self, question_id: str, answer: bool, feature_map: Dict[str, bool]):
        """Update planet probabilities based on the user's answer."""
        self.update_probabilities_based_on_answer(answer, feature_map)

        # Normalize probabilities after adjustments
        total = sum(self.possible_planets.values())
        
        # Print updated probabilities elegantly
        print("\nUpdated Probabilities:")
        
        if total > 0:
            for planet in self.possible_planets:
                self.possible_planets[planet] /= total
                print(f"{planet}: {self.possible_planets[planet]:.4f}")
        else:
            print("All planet probabilities have been eliminated.")

    def update_probabilities_based_on_answer(self, answer: bool, feature_map: Dict[str, bool]):
        """Update probabilities based on the user's answer to a question."""
        
        if answer:  # If the answer is yes
            for planet in self.possible_planets.keys():
                if feature_map[planet]:  # If this planet has the attribute set to true
                    self.possible_planets[planet] *= 2.0  # Boost probability for true attributes
                else:
                    # Instead of setting to zero, reduce probability by a certain factor
                    self.possible_planets[planet] *= 0.1  # Reduce but retain some probability

        else:  # If the answer is no
            for planet in self.possible_planets.keys():
                if not feature_map[planet]:  # If this planet does not have the attribute set to true
                    self.possible_planets[planet] *= 2.0  # Boost probability for false attributes
                else:
                    # Again reduce but retain some probability
                    self.possible_planets[planet] *= 0.1  # Reduce but retain some probability
    def calculate_entropy(self, probabilities: Dict[str, float]) -> float:
        """Calculate the entropy of a probability distribution."""
        from math import log2
        return -sum(p * log2(p) for p in probabilities.values() if p > 0)

    def ask_question(self) -> Optional[tuple]:
        """Select the next most informative question to ask."""
        remaining_questions = [q for q in self.questions if q[0] not in self.asked_questions]
        
        if not remaining_questions:
            return None

        question_gains = [(self.calculate_information_gain(q), q) for q in remaining_questions]
        
        best_question = max(question_gains, key=lambda x: x[0])[1]
        
        return best_question

    def calculate_information_gain(self, question: tuple) -> float:
        """Calculate information gain for a given question."""
        feature_map = question[2]
        total_entropy = self.calculate_entropy(self.possible_planets)
        
        yes_probs = {planet: self.possible_planets[planet] for planet in feature_map if feature_map[planet]}
        no_probs = {planet: self.possible_planets[planet] for planet in feature_map if not feature_map[planet]}
        
        yes_entropy = self.calculate_entropy(yes_probs)
        no_entropy = self.calculate_entropy(no_probs)

        total_possible = sum(self.possible_planets.values())
        
        if total_possible == 0:
            return 0

        weight_yes = sum(yes_probs.values()) / total_possible
        weight_no = sum(no_probs.values()) / total_possible
        
        information_gain = total_entropy - (weight_yes * yes_entropy + weight_no * no_entropy)
        
        return information_gain

    def get_most_likely_planet(self) -> str:
        """Return the planet with the highest probability."""
        return max(self.possible_planets.items(), key=lambda x: x[1])[0]

    def play_game(self):
        """Main game loop for the planet guessing game."""
        print("Think of a planet in our solar system, and I'll try to guess it!")
        print("Please answer with either y (yes) or n (no).\n")

        while True:
            max_prob = max(self.possible_planets.values())
            
            if max_prob > 0.8:
                guess = self.get_most_likely_planet()
                
                print(f"\nI think it's {guess}! Am I right? (y/n)")
                
                answer = input().lower().strip()
                
                if answer.startswith('y'):
                    print("Great! I guessed it!")
                    return
                elif answer.startswith('n'):
                    # Reduce probability for wrong guess
                    self.possible_planets[guess] *= 0.5
                    continue
                else:
                    print("Please respond with y or n.")
                    continue

            next_question = self.ask_question()
            
            if not next_question:
                guess = self.get_most_likely_planet()
                
                print(f"\nI'm not entirely sure; but is it {guess}? (y/n)")
                
                answer = input().lower().strip()
                
                if answer.startswith('y'):
                    print("Great! I guessed it!")
                    return
                elif answer.startswith('n'):
                    print("Thanks for playing!")
                    return
                else:
                    print("Please respond with y or n.")
                    continue

            question_id, question_text, feature_map = next_question
            
            print(f"\n{question_text} (y/n)")
            
            answer = input().lower().strip()
            
            if answer not in ['y', 'n']:
                print("Please answer with either y or n.")
                continue
            
            # Update probabilities based on user response
            self.update_probabilities(
                question_id,
                answer == "y",
                feature_map
            )
            
            self.asked_questions.add(question_id)
            self.question_count += 1  # Increment question count

if __name__ == "__main__":
    expert = SolarSystemExpert()
    expert.play_game()