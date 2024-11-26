from experta import KnowledgeEngine
from typing import Dict, List, Optional
import math
import random
from facts import (
    Sun, Mercury, Venus, Earth, Mars, 
    Jupiter, Saturn, Uranus, Neptune
)

class SolarSystemExpert(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        # Initialize probabilities equally
        self.possible_planets = {
            'Mercury': 0.125, 
            'Venus': 0.125, 
            'Earth': 0.125, 
            'Mars': 0.125, 
            'Jupiter': 0.125, 
            'Saturn': 0.125, 
            'Uranus': 0.125, 
            'Neptune': 0.125
        }
        
        # Hierarchical questions organized by tiers
        self.questions = {
            1: [  # Broadest, most distinguishing questions
                ("is_gas_giant", "Is it a gas giant?", {
                    'Jupiter': True, 'Saturn': True, 'Uranus': True, 'Neptune': True,
                    'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
                }),
                ("is_inner_planet", "Is it one of the inner planets (closer to the Sun)?", {
                    'Mercury': True, 'Venus': True, 'Earth': True, 'Mars': True,
                    'Jupiter': False, 'Saturn': False, 'Uranus': False, 'Neptune': False
                }),
            ],
            2: [  # More specific questions
                ("has_atmosphere", "Does it have a substantial atmosphere?", {
                    'Venus': True, 'Earth': True, 'Jupiter': True, 'Saturn': True,
                    'Uranus': True, 'Neptune': True, 'Mars': False, 'Mercury': False
                }),
                ("has_rings", "Does it have prominent rings?", {
                    'Saturn': True, 'Uranus': True, 'Jupiter': True, 'Neptune': True,
                    'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
                }),
            ],
            3: [  # Most specific, nuanced questions
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
                }),
            ]
        }
        
        # Tracking question-asking process
        self.current_tier = 1
        self.asked_questions = set()
        
    def calculate_entropy(self, probabilities: List[float]) -> float:
        """Calculate entropy from a list of probabilities."""
        return -sum(p * math.log2(p) for p in probabilities if p > 0)
    
    def compute_question_information_gain(self, feature_map: Dict[str, bool]) -> float:
        """
        Calculate the information gain of a question.
        Higher value means the question is more informative.
        """
        true_planets = []
        false_planets = []
        
        for planet, probability in self.possible_planets.items():
            if feature_map[planet]:
                true_planets.append(probability)
            else:
                false_planets.append(probability)
        
        total_prob = sum(true_planets) + sum(false_planets)
        
        # If no probabilities, return 0
        if total_prob == 0:
            return 0
        
        # Compute probabilities of true and false groups
        true_prob = sum(true_planets) / total_prob
        false_prob = sum(false_planets) / total_prob
        
        # Information gain is highest when probabilities are close to 0.5
        # This means the question divides the possibilities most evenly
        return 1 - abs(true_prob - 0.5) * 2
    
    def ask_question(self) -> Optional[tuple]:
        """
        Intelligently select the next most informative question.
        Prioritizes current tier and selects based on information gain.
        """
        # Get unasked questions from current tier
        remaining_questions = [
            q for q in self.questions[self.current_tier] 
            if q[0] not in self.asked_questions
        ]
        
        # If no questions left in current tier, move to next
        if not remaining_questions:
            self.current_tier += 1
            
            # If all tiers exhausted, return None
            if self.current_tier > max(self.questions.keys()):
                return None
            
            # Recursively try to get a question from the next tier
            return self.ask_question()
        
        # Compute information gain for each remaining question
        question_gains = []
        for question in remaining_questions:
            gain = self.compute_question_information_gain(question[2])
            question_gains.append((gain, question))
        
        # Select the question with the highest information gain
        if question_gains:
            return max(question_gains, key=lambda x: x[0])[1]
        
        return None
    
    def update_probabilities(self, question_id: str, answer: bool, feature_map: Dict[str, bool]):
        """Update planet probabilities based on the user's answer."""
        for planet, probability in self.possible_planets.items():
            if feature_map[planet] == answer:
                # Reduce probability for planets that match the answer
                self.possible_planets[planet] *= 0.9
            else:
                # Significantly reduce probability for non-matching planets
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