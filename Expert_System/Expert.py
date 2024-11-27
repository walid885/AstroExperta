"""from typing import Dict, Optional, List, Tuple
import math

class SolarSystemExpert:
    def __init__(self):
        self.possible_planets = {
            'Mercury': 1.0 / 8, 'Venus': 1.0 / 8, 'Earth': 1.0 / 8, 'Mars': 1.0 / 8,
            'Jupiter': 1.0 / 8, 'Saturn': 1.0 / 8, 'Uranus': 1.0 / 8, 'Neptune': 1.0 / 8
        }
        self.questions = [
            ("has_moons", "Does it have significant moons?", {
                'Earth': True, 'Mars': True, 'Jupiter': True, 'Saturn': True,
                'Uranus': True, 'Neptune': True,
                'Mercury': False, 'Venus': False
            }),
            ("has_atmosphere", "Does it have a substantial atmosphere?", {
                'Venus': True, 'Earth': True, 'Jupiter': True, 'Saturn': True,
                'Uranus': True, 'Neptune': True, 'Mars': False, 'Mercury': False
            }),
            ("has_rings", "Does it have prominent rings?", {
                'Saturn': True, 'Uranus': True, 'Jupiter': True, 'Neptune': True,
                'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
            }),
            ("is_gas_giant", "Is it a gas giant?", {
                'Jupiter': True, 'Saturn': True, 'Uranus': True, 'Neptune': True,
                'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
            }),
            ("is_inner_planet", "Is it one of the inner planets (closer to the Sun)?", {
                'Mercury': True, 'Venus': True, 'Earth': True, 'Mars': True,
                'Jupiter': False, 'Saturn': False, 'Uranus': False, 'Neptune': False
            }),
            ("is_habitable", "Is it potentially habitable or known to harbor life?", {
                'Earth': True,
                'Mercury': False,
                'Venus': False,
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
            })
        ]
        self.asked_questions = []
        self.true_questions = []
    def check_direct_facts(self):
        """"""Check for directly known facts before asking questions."""
        """if len([p for p, v in self.possible_planets.items() if p == 'Earth' and v > 0.9]) > 0:
            print("Earth is the only known planet in our solar system that harbors life.")
            return True
        return False



    def update_probabilities(self, question_id: str, answer: bool, feature_map: Dict[str, bool]):
        """"""Update planet probabilities based on the user's answer."""
        """eliminated_planets = []
        true_planets = []

        for planet in list(self.possible_planets.keys()):
            if feature_map[planet] == answer:
                self.possible_planets[planet] *= 1.5
                true_planets.append(planet)
            else:
                eliminated_planets.append(planet)
                self.possible_planets[planet] *= 0.5
        
        # Normalize probabilities
        total = sum(self.possible_planets.values())
        
        if total > 0:
            for planet in self.possible_planets:
                self.possible_planets[planet] /= total

        # Print eliminated and true planets after each answer
        print("\nEliminated Planets:", ", ".join(eliminated_planets))
        print("True Planets:", ", ".join(true_planets))

    def track_candidates(self):
        """T"""rack and print candidate planets based on true questions"""
        """print("\n" + "="*50)
        print("CANDIDATE PLANET ANALYSIS")
        print("="*50)

        # Sort planets by probability in descending order
        sorted_planets = sorted(
            self.possible_planets.items(), 
            key=lambda x: x[1], 
            reverse=True
        )

        # Print overall current probabilities
        print("\nCurrent Planet Probabilities:")
        for planet, prob in sorted_planets:
            print(f"{planet}: {prob:.4f}")

    def ask_question(self) -> Optional[tuple]:
        """"""Select the next most informative question to ask."""
        """remaining_questions = [q for q in self.questions if q[0] not in [aq[0] for aq in self.asked_questions]]
        
        if not remaining_questions:
            return None

        return remaining_questions[0]

    def play_game(self):
        """"""Main game loop for the planet guessing game."""
        """print("Think of a planet in our solar system, and I'll try to guess it!")
        print("Please answer with 'yes' or 'no'.\n")

        while True:
            # Track current candidates
            self.track_candidates()

            # Check if any planet has a high enough probability to guess
            max_prob = max(self.possible_planets.values())
            
            if max_prob > 0.75:
                guess = max(self.possible_planets.items(), key=lambda x: x[1])[0]
                print(f"\nI think it's {guess}! Am I right? (yes/no)")
                
                answer = input().lower().strip()
                
                if answer.startswith('y'):
                    print("Great! I guessed it!")
                    self.track_candidates()
                    return
                else:
                    # Reduce probability for wrong guess
                    self.possible_planets[guess] *= 0.1
                    continue

            # Ask next question
            next_question = self.ask_question()
            
            if not next_question:
                guess = max(self.possible_planets.items(), key=lambda x: x[1])[0]
                print(f"\nI'm not entirely sure; is it {guess}?")
                self.track_candidates()
                return

            question_id, question_text, feature_map = next_question
            
            print(f"\n{question_text}")
            
            answer = input().lower().strip()
            
            if answer not in ['yes', 'no']:
                print("Please answer with either 'yes' or 'no'.")
                continue
            
            # Update asked questions and true questions if applicable
            self.asked_questions.append((question_id, answer == "yes"))
            
            # Update probabilities based on answer
            self.update_probabilities(
                question_id,
                answer == "yes",
                feature_map
            )

if __name__ == "__main__":
    expert = SolarSystemExpert()
    expert.play_game()"""