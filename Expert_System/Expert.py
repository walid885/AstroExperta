class PlanetGuessingExpert:
    def __init__(self):
        # More balanced initial approach
        self.possible_planets = {
            'Mercury': 1/8, 'Venus': 1/8, 'Earth': 1/8, 'Mars': 1/8, 
            'Jupiter': 1/8, 'Saturn': 1/8, 'Uranus': 1/8, 'Neptune': 1/8
        }
        
        # Reorganize questions to start with the MOST BROAD and DISTINGUISHING questions
        self.questions = {
            1: [  # MOST BROAD distinguishing questions
                ("is_inner_planet", "Is it one of the inner planets (closer to the Sun)?", {
                    'Mercury': True, 'Venus': True, 'Earth': True, 'Mars': True,
                    'Jupiter': False, 'Saturn': False, 'Uranus': False, 'Neptune': False
                }),
                ("is_gas_giant", "Is it a gas giant?", {
                    'Jupiter': True, 'Saturn': True, 'Uranus': True, 'Neptune': True,
                    'Mercury': False, 'Venus': False, 'Earth': False, 'Mars': False
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
                ("has_moons", "Does it have significant moons?", {
                    'Earth': True, 'Mars': True, 'Jupiter': True, 'Saturn': True,
                    'Uranus': True, 'Neptune': True,
                    'Mercury': False, 'Venus': False
                }),
            ]
        }
        
        self.current_tier = 1
        self.asked_questions = set()
    
    def select_initial_question(self):
        """
        Strategically select the first, most broad question
        """
        # Start with the most distinguishing broad questions
        return self.questions[1][0]
    
    def ask_question(self):
        """
        Intelligently select the next most informative question
        """
        # If no questions have been asked yet, start with the broadest question
        if not self.asked_questions:
            return self.select_initial_question()
        
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
    
    def compute_question_information_gain(self, feature_map):
        """
        Calculate information gain that favors questions 
        that most effectively divide the search space
        """
        # Count how many planets would answer 'yes' and 'no'
        yes_planets = sum(1 for planet, val in feature_map.items() if val)
        no_planets = sum(1 for planet, val in feature_map.items() if not val)
        
        # Prefer questions that divide the planets most evenly
        balance_score = 1 - abs(yes_planets - no_planets) / len(feature_map)
        
        return balance_score
    
    def update_probabilities(self, question, answer):
        """
        Update planet probabilities based on the question and answer
        """
        for planet in list(self.possible_planets.keys()):
            # If the answer matches the planet's feature, keep the planet
            # If not, remove or significantly reduce its probability
            if question[2][planet] == (answer.lower() == 'yes'):
                # Increase probability slightly
                self.possible_planets[planet] *= 1.5
            else:
                # Dramatically reduce or remove probability
                del self.possible_planets[planet]
        
        # Normalize remaining probabilities
        if self.possible_planets:
            total = sum(self.possible_planets.values())
            self.possible_planets = {p: prob/total for p, prob in self.possible_planets.items()}
        
        return self.possible_planets

# Main game logic
def play_planet_guessing_game():
    expert = PlanetGuessingExpert()
    
    print("Think of a planet in our solar system, and I'll try to guess it!")
    print("Please answer with 'yes' or 'no'.")
    
    while True:
        # Select and ask the next question
        current_question = expert.ask_question()
        
        # If no more questions, attempt to guess
        if current_question is None:
            if len(expert.possible_planets) == 1:
                planet = list(expert.possible_planets.keys())[0]
                print(f"Is it {planet}? (yes/no)")
                answer = input().lower()
                if answer == 'yes':
                    print("I guessed the planet!")
                    break
                else:
                    print("I'm out of questions and guesses!")
                    break
            else:
                print("I'm having trouble narrowing down the planet!")
                break
        
        # Ask the selected question
        print(current_question[1])
        answer = input().lower()
        
        # Update the asked questions and probabilities
        expert.asked_questions.add(current_question[0])
        expert.update_probabilities(current_question, answer)
        
        # Debug: Print remaining possible planets
        print("Possible planets:", list(expert.possible_planets.keys()))

# Run the game
if __name__ == "__main__":
    play_planet_guessing_game()