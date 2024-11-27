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
                'Jupiter': True, 'Saturn': True, 'Uranus': True, 'Neptune': True,
                'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
            }),
            ("has_rings", "Does it have prominent rings?", {
                'Saturn': True, 'Uranus': True, 'Jupiter': True, 'Neptune': True,
                'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
            }),
            ("is_inner_planet", "Is it one of the inner planets (closer to the Sun)?", {
                'Mercury': True, 'Venus': True, 'Earth': True, 'Mars': True,
                'Jupiter': False, 'Saturn': False, 'Uranus': False, 'Neptune': False
            }),
            ("has_atmosphere", "Does it have a substantial atmosphere?", {
                'Venus': True, 'Earth': True,
                'Jupiter': True, 'Saturn': True,
                'Uranus': True, 'Neptune': True,
                'Mars': False, 'Mercury': False
            }),
            ("is_habitable", "Is it potentially habitable or known to harbor life?", {
                'Earth': True,
                'Mercury': False, 'Venus': False,
                'Mars': False,
                'Jupiter': False,
                'Saturn': False,
                'Uranus': False,
                'Neptune': False
            }),
            ("extreme_temp", "Is it known for extreme temperatures?", {
                'Mercury': True,
                'Venus': True,
                'Earth': False,
                'Mars': False,
                'Jupiter': False,
                'Saturn': False,
                'Uranus': False,
                'Neptune': False
            }),
            ("has_moons", "Does it have significant moons?", {
                'Earth': True,
                'Mars': True,
                'Jupiter': True,
                'Saturn': True,
                'Uranus': True,
                'Neptune': True,
                'Mercury': False,
                'Venus': False
            })
        ]
        self.asked_questions = set()

    def update_probabilities(self, question_id: str, answer: bool, feature_map: Dict[str, bool]):
        """Update planet probabilities based on the user's answer."""
        if answer:  # If the answer is yes
            self.boost_probabilities(feature_map)
        else:  # If the answer is no
            self.reduce_probabilities(feature_map)

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

    def boost_probabilities(self, feature_map: Dict[str, bool]):
        """Boost probabilities for planets that match the feature map."""
        for planet in self.possible_planets.keys():
            if feature_map[planet]:  # If this planet has the attribute set to true
                self.possible_planets[planet] *= 1.5  # Increase probability by a factor

    def reduce_probabilities(self, feature_map: Dict[str, bool]):
        """Reduce probabilities of planets that do not match the feature map."""
        for planet in self.possible_planets.keys():
            if not feature_map[planet]:  # If this planet does not have the attribute set to true
                self.possible_planets[planet] *= 0.5  # Decrease probability by a factor

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
        print("Please answer with 'yes' or 'no'.\n")

        while True:
            max_prob = max(self.possible_planets.values())
            
            if max_prob > 0.8:
                guess = self.get_most_likely_planet()
                
                print(f"\nI think it's {guess}! Am I right? (yes/no)")
                
                answer = input().lower().strip()
                
                if answer.startswith('y'):
                    print("Great! I guessed it!")
                    return
                else:
                    # Reduce probability for wrong guess
                    self.possible_planets[guess] *= 0.5
                    continue

            next_question = self.ask_question()
            
            if not next_question:
                guess = self.get_most_likely_planet()
                
                print(f"\nI'm not entirely sure; but is it {guess}?")
                
                return

            question_id, question_text, feature_map = next_question
            
            print(f"\n{question_text}")
            
            answer = input().lower().strip()
            
            if answer not in ['yes', 'no']:
                print("Please answer with either yes or no.")
                continue
            
            # Update probabilities based on user response
            self.update_probabilities(
                question_id,
                answer == "yes",
                feature_map
            )
            
            self.asked_questions.add(question_id)

if __name__ == "__main__":
    expert = SolarSystemExpert()
    expert.play_game()