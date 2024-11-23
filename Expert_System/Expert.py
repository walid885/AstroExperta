import random
from typing import Dict, Optional
from Expert_System import knowledge_engine


class SolarSystemExpert(knowledge_engine):
    def __init__(self):
        super().__init__()
        self.possible_planets = {
            'Mercury': 1.0, 'Venus': 1.0, 'Earth': 1.0, 'Mars': 1.0,
            'Jupiter': 1.0, 'Saturn': 1.0, 'Uranus': 1.0, 'Neptune': 1.0
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
                'Venus': True, 'Earth': True, 'Jupiter': True, 'Saturn': True,
                'Uranus': True, 'Neptune': True, 'Mars': False, 'Mercury': False
            }),
            ("is_habitable", "Is it potentially habitable or known to harbor life?", {
                'Earth': True,
                'Mercury': False, 'Venus': False, 'Mars': False,
                'Jupiter': False, 'Saturn': False, 'Uranus': False, 'Neptune': False
            }),
            ("extreme_temp", "Is it known for extreme temperatures?", {
                'Mercury': True, 'Venus': True,
                'Earth': False, 'Mars': False, 'Jupiter': False,
                'Saturn': False, 'Uranus': False, 'Neptune': False
            }),
            ("has_moons", "Does it have significant moons?", {
                'Earth': True, 'Mars': True, 'Jupiter': True, 'Saturn': True,
                'Uranus': True, 'Neptune': True,
                'Mercury': False, 'Venus': False
            })
        ]
        self.asked_questions = set()
        
    def ask_question(self) -> Optional[tuple]:
        """Select the next most informative question to ask."""
        remaining_questions = [q for q in self.questions if q[0] not in self.asked_questions]
        if not remaining_questions:
            return None
        
        return random.choice(remaining_questions)
    
    def update_probabilities(self, question_id: str, answer: bool, feature_map: Dict[str, bool]):
        """Update planet probabilities based on the user's answer."""
        for planet, probability in self.possible_planets.items():
            if feature_map[planet] == answer:
                self.possible_planets[planet] *= 0.9
            else:
                self.possible_planets[planet] *= 0.1
                
        # Normalize probabilities
        total = sum(self.possible_planets.values())
        if total > 0:
            for planet in self.possible_planets:
                self.possible_planets[planet] /= total

    def get_most_likely_planet(self) -> str:
        """Return the planet with the highest probability."""
        return max(self.possible_planets.items(), key=lambda x: x[1])[0]

    def play_game(self):
        """Main game loop for the planet guessing game."""
        print("Think of a planet in our solar system, and I'll try to guess it!")
        print("Please answer with 'yes' or 'no'.\n")

        while True:
            # Get the most likely planet if probability is high enough
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
                    self.possible_planets[guess] *= 0.1
                    continue

            # Ask next question
            next_question = self.ask_question()
            if not next_question:
                # If no more questions, make a final guess
                guess = self.get_most_likely_planet()
                print(f"\nI'm not entirely sure, but is it {guess}?")
                return

            question_id, question_text, feature_map = next_question
            print(f"\n{question_text}")
            answer = input().lower().strip()
            
            # Update probabilities based on answer
            self.update_probabilities(
                question_id,
                answer.startswith('y'),
                feature_map
            )
            self.asked_questions.add(question_id)

if __name__ == "__main__":
    expert = SolarSystemExpert()
    expert.play_game()
