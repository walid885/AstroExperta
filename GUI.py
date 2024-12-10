import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Expert_System.knlowledge_engineGUIntegr import SolarSystemExpertGUI  # Ensure correct import

class AstronomyExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("AstroAcademy Expert System")
        self.root.geometry("1400x800")  # Increased window size to accommodate new frame
        
        # Enhanced color scheme (previous colors remain the same)
        self.colors = {
            'bg_dark': '#0B1026',      # Deep space blue
            'bg_medium': '#1B2559',    # Midnight blue
            'accent': '#4B61D1',       # Stellar blue
            'text': '#E6E8F0',         # Starlight white
            'highlight': '#8B9EF0',    # Nebula purple
            'background_soft': '#2C3E50',  # Soft dark background
            'success_green': '#2ECC71',    # Success green
            'warning_yellow': '#F39C12'    # Warning yellow
        }
        
        # Configure the root window
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Initialize the expert system
        self.expert_system = SolarSystemExpertGUI()
        
        # Configure styles
        self.setup_styles()
        
        # Configure grid layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create main frame with three columns
        self.main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="30")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)  # Visualization
        self.main_frame.grid_columnconfigure(1, weight=1)  # Question
        self.main_frame.grid_columnconfigure(2, weight=1)  # Thinking Frame
        
        # Title Label
        title_font = tkFont.Font(family="Helvetica", size=28, weight="bold")
        self.title_label = tk.Label(
            self.main_frame,
            text="✧ AstroAcademy Expert System ✧",
            font=title_font,
            bg=self.colors['bg_dark'],
            fg=self.colors['text']
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=(0, 30), sticky="ew")
        
        # Left Column - Probability Visualization Frame
        self.visualization_frame = ttk.LabelFrame(
            self.main_frame,
            text="Probability Visualization",
            style='Visualization.TLabelframe',
            padding="20"
        )
        self.visualization_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        # Placeholder for matplotlib canvas
        self.canvas_frame = ttk.Frame(self.visualization_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)
        
        # Middle Column - Question Frame
        self.question_frame = ttk.LabelFrame(
            self.main_frame,
            text="Your Cosmic Quest",
            style='Question.TLabelframe',
            padding="20"
        )
        self.question_frame.grid(row=1, column=1, sticky="nsew", padx=10, pady=10)
        
        # Question Label
        self.question_label = ttk.Label(
            self.question_frame,
            text="🌟 Think of a celestial object and press Start! 🌟",
            style='Question.TLabel',
            font=("Helvetica", 16)
        )
        self.question_label.pack(pady=20, expand=True)
        
        # Buttons Frame within Question Frame
        self.buttons_frame = ttk.Frame(self.question_frame, style='Main.TFrame')
        self.buttons_frame.pack(pady=20)
        
        # Buttons
        self.start_button = ttk.Button(
            self.buttons_frame,
            text="Start Journey",
            style='Start.TButton',
            command=self.start_game,
            
        )
        self.start_button.grid(row=0, column=1, padx=10)
        
        self.yes_button = ttk.Button(
            self.buttons_frame,
            text="Yes",
            style='Yes.TButton',  # Changed from 'Answer.TButton'
            command=lambda: self.process_answer(True),
            state="disabled"
        )
        self.yes_button.grid(row=0, column=0, padx=10)

        
        self.no_button = ttk.Button(
            self.buttons_frame,
            text="No",
            style='No.TButton',  # Changed from 'Answer.TButton'
            command=lambda: self.process_answer(False),
            state="disabled"
        )
        self.no_button.grid(row=0, column=2, padx=10)

        
        # Right Column - Thinking Frame
        self.thinking_frame = ttk.LabelFrame(
            self.main_frame,
            text="System's Thought Process",
            style='Thinking.TLabelframe',
            padding="20"
        )
        self.thinking_frame.grid(row=1, column=2, sticky="nsew", padx=10, pady=10)
        
        # Thinking Label
        self.thinking_label = ttk.Label(
            self.thinking_frame,
            text="🤔 THINKING... 🌌",
            style='Thinking.TLabel',
            font=("Helvetica", 16, "bold")
        )
        self.thinking_label.pack(pady=20, expand=True)


        
        # Probability Label in Thinking Frame
        self.probability_label = ttk.Label(
            self.thinking_frame,
            text="Current Probabilities: ",
            style='Probability.TLabel',
            font=("Helvetica", 12)
        )
        self.probability_label.pack(pady=20)
        self.initialize_histogram()
        self.reset_button = ttk.Button(
        self.buttons_frame,
        text="Reset Game",
        style='Reset.TButton',
        command=self.reset_game,
        state="disabled"
    )
        
        self.reset_button.grid(row=1, column=1, padx=10, pady=(10, 0))






    def setup_styles(self):
        """Configure custom styles for the application"""
        style = ttk.Style()
        style.configure('Main.TFrame', background=self.colors['bg_dark'])
        style.configure('Question.TLabelframe', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Visualization.TLabelframe', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Question.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Probability.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['highlight'],
                       font=('Helvetica', 12, 'bold'))
        style.configure('Start.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 12, 'bold'),
                       padding=10)
        style.configure('Answer.TButton',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 12),
                       padding=10)
        style.configure('Thinking.TLabelframe', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Thinking.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['highlight'],
                       font=('Helvetica', 16, 'bold'))
        style.configure('Reset.TButton',
                         background=self.colors['warning_yellow'], 
                         foreground=self.colors['text'], 
                         font=('Helvetica', 12), padding=10)
        style.configure('Yes.TButton',
                    background=self.colors['success_green'],
                    foreground=self.colors['text'],
                    font=('Helvetica', 12, 'bold'),
                    padding=10)
        style.map('Yes.TButton', 
              background=[('disabled', self.colors['bg_medium'])],
              foreground=[('disabled', self.colors['text'])])

    # No button style - use a red tone that fits the color palette
        style.configure('No.TButton',
                    background='#E74C3C',  # A vibrant red that complements the existing palette
                    foreground=self.colors['text'],
                    font=('Helvetica', 12, 'bold'),
                    padding=10)
        style.map('No.TButton', 
              background=[('disabled', self.colors['bg_medium'])],
              foreground=[('disabled', self.colors['text'])])



    def process_answer(self, answer):
        """Process user answers and update game state."""
        print(f"User answered {'Yes' if answer else 'No'}.")
        
        if hasattr(self, 'current_feature_map'):
            feature_map = self.current_feature_map  
            question_id = self.current_question_id  
            print(f"Processing answer for question ID: {question_id}")

            # Update probabilities based on user response (yes/no)
            self.expert_system.update_probabilities(question_id, answer, feature_map)

            next_question = self.expert_system.get_next_question()
            
            if next_question:
                question_id, question_text, feature_map = next_question  
                self.current_question_id = question_id  
                self.current_feature_map = feature_map  

                self.question_label.config(text=question_text)  
                # Reset thinking label to thinking state
                self.reset_thinking_label()

            else:
                guess = self.expert_system.get_most_likely_planet()  
                
                # Update thinking label with the guess
                if guess == "Earth":
                    self.update_thinking_label(
                        f"🌍 I think it is {guess}! ✨", 
                        color=self.colors['success_green']
                    )
                else:
                    self.update_thinking_label(
                        f"🤔 I think it is {guess}!", 
                        color=self.colors['warning_yellow']
                    )

                # Disable answer buttons after game completion
                self.yes_button.config(state="disabled")
                self.no_button.config(state="disabled")
                self.start_button.config(state="normal")

            # Update probabilities display after processing answer.
            self.update_probabilities_display()
            # Update histogram after processing answer.
            self.update_histogram()


    def show_result_banner(self, message, color=None):
        """Display a message in the result banner with optional color."""
        self.result_banner.config(
            text=message, 
            bg=color or self.colors['bg_medium']
        )

    def reset_result_banner(self):
        """Reset the result banner to its default state."""
        self.result_banner.config(
            text="",
            bg=self.colors['bg_medium']
        )

    def reset_game(self):
        self.expert_system.reset_game()
        self.update_histogram()  # Use update_histogram instead of initialize_histogram
        self.question_label.config(text="🌟 Think of a celestial object and press Start! 🌟")
        self.start_button.config(state="normal")
        self.yes_button.config(state="disabled")
        self.no_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.reset_thinking_label()
        self.update_probabilities_display()

    
    def update_thinking_label(self, message, color=None):
        """Update the thinking label with a specific message and optional color."""
        self.thinking_label.config(
            text=message, 
            foreground=color or self.colors['text']
        )

    def reset_thinking_label(self):
        """Reset the thinking label to its default state."""
        self.thinking_label.config(
            text="🤔 THINKING... 🌌",
            foreground=self.colors['highlight']
        )


    def create_histogram(self, df):
        plt.figure(figsize=(8, 6), dpi=100, facecolor=self.colors['bg_medium'])
        plt.style.use('dark_background')
        ax = sns.barplot(
            x='Celestial Object', y='Probability', data=df,
            palette='viridis', hue='Celestial Object', dodge=False, legend=False
        )
        
        plt.title('Probability of Celestial Objects', color=self.colors['text'], fontsize=16, fontweight='bold')
        plt.xlabel('Celestial Objects', color=self.colors['text'])
        plt.ylabel('Probability', color=self.colors['text'])
        plt.xticks(rotation=45, color=self.colors['text'])
        plt.yticks(color=self.colors['text'])
        
        for i, v in enumerate(df['Probability']):
            ax.text(i, v, f'{v:.4f}', ha='center', va='bottom', color=self.colors['text'], fontweight='bold')
        
        plt.tight_layout()
        
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        canvas.draw()
        plt.close()



    def update_histogram(self):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        fixed_objects = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        all_probabilities = {obj: 0.125 for obj in fixed_objects}  # Equal probability for reset
        all_probabilities.update(self.expert_system.possible_planets)
        df = pd.DataFrame({
            'Celestial Object': fixed_objects,
            'Probability': [all_probabilities[obj] for obj in fixed_objects]
        })
        self.create_histogram(df)

    def initialize_histogram(self):
        fixed_objects = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        initial_probabilities = {obj: 0.125 for obj in fixed_objects}  # Equal probability for all objects
        
        df = pd.DataFrame({
            'Celestial Object': fixed_objects,
            'Probability': [initial_probabilities[obj] for obj in fixed_objects]
        })
        
        self.create_histogram(df)


    def start_game(self):
        self.expert_system.reset_game()
        self.initialize_histogram()
        question = self.expert_system.get_next_question()
        if question:
            question_id, question_text, feature_map = question
            self.current_question_id = question_id
            self.current_feature_map = feature_map
            self.question_label.config(text=question_text)
            self.start_button.config(state="disabled")
            self.yes_button.config(state="normal")
            self.no_button.config(state="normal")
            self.reset_button.config(state="normal")  # Enable reset button
            self.reset_thinking_label()
            self.update_probabilities_display()
            self.update_histogram()


    def process_answer(self, answer):
        """Process user answers and update game state."""
        print(f"User answered {'Yes' if answer else 'No'}.")
        
        if hasattr(self, 'current_feature_map'):
            feature_map = self.current_feature_map  
            question_id = self.current_question_id  
            print(f"Processing answer for question ID: {question_id}")

            # Update probabilities based on user response (yes/no)
            self.expert_system.update_probabilities(question_id, answer, feature_map)

            next_question = self.expert_system.get_next_question()
            
            if next_question:
                question_id, question_text, feature_map = next_question  
                self.current_question_id = question_id  
                self.current_feature_map = feature_map  

                self.question_label.config(text=question_text)  
                # Reset thinking label to thinking state
                self.reset_thinking_label()

            else:
                guess = self.expert_system.get_most_likely_planet()  
                
                # Update thinking and buttons for game completion
                self.update_final_guess(guess)

            # Update probabilities display after processing answer.
            self.update_probabilities_display()
            # Update histogram after processing answer.
            self.update_histogram()
    def update_final_guess(self, guess):
            """
            Elegantly display the final guess with enhanced visual and informative feedback.
            
            Provides a comprehensive breakdown of the guess, including:
            - Planet emoji
            - Confidence level
            - Detailed probability explanation
            """
            planet_emojis = {
                "Mercury": "☿", "Venus": "♀", 
                "Earth": "🌍", "Mars": "♂",
                "Jupiter": "♃", "Saturn": "♄", 
                "Uranus": "⛢", "Neptune": "♆"
            }

            emoji = planet_emojis.get(guess, "🌠")
            confidence = self.expert_system.possible_planets.get(guess, 0)
            
            # Create a more detailed probability breakdown
            probabilities = self.expert_system.possible_planets
            sorted_probabilities = sorted(probabilities.items(), key=lambda x: x[1], reverse=True)
            
            # Generate a detailed probability explanation
            prob_explanation = "Probability Breakdown:\n"
            for planet, prob in sorted_probabilities[:3]:  # Show top 3 most likely planets
                prob_explanation += f"{planet}: {prob*100:.2f}%\n"

            # Determine confidence message based on probability
            if confidence >= 0.8:
                confidence_message = "High Confidence! 🌟"
                color = self.colors['success_green']
            elif confidence >= 0.5:
                confidence_message = "Moderate Confidence 🔍"
                color = self.colors['highlight']
            else:
                confidence_message = "Low Confidence 🤨"
                color = self.colors['warning_yellow']

            # Comprehensive thinking label
            full_message = (
                f"🎯 Final Guess: {guess} {emoji}\n"
                f"{confidence_message} (Confidence: {confidence*100:.2f}%)\n\n"
                f"{prob_explanation}"
            )

            # Update thinking label with comprehensive information
            self.update_thinking_label(full_message, color=color)

            # Disable/enable buttons appropriately
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
            self.start_button.config(state="normal")
            self.reset_button.config(state="normal")    


    def setup_emoji_font(self):
        # Use a font that supports emojis
        emoji_font = tkFont.Font(family="Segoe UI Emoji", size=12)
        self.probability_label.configure(font=emoji_font)

    def update_probabilities_display(self):
        probabilities_text = "Current Probabilities:\n"
        for planet, prob in sorted(self.expert_system.possible_planets.items(), key=lambda x: x[1], reverse=True):
            probabilities_text += f"{planet}: {prob:.4f}\n"
        
        if max(self.expert_system.possible_planets.values()) > 0.8:
            guess_planet = max(self.expert_system.possible_planets.items(), key=lambda x: x[1])[0]
            probabilities_text += f"\n\U0001F680 BREAKING NEWS: I MIGHT GUESS: {guess_planet.upper()}! \U00002B50"
        
        self.probability_label.config(text=probabilities_text)

    def update_guess_thinking(self, probabilities, threshold=0.8):
        """
        Update the thinking label with an enthusiastic guess when a planet's 
        probability exceeds the threshold.
        """
        planet_emojis = {
            "Mercury": "☿", "Venus": "♀", "Earth": "🌍", "Mars": "♂",
            "Jupiter": "♃", "Saturn": "♄", "Uranus": "⛢", "Neptune": "♆"
        }
        
        for planet, prob in probabilities.items():
            if prob >= threshold:
                guess_message = f"Eureka! I think IT'S {planet.upper()}! {planet_emojis[planet]}"
                self.update_thinking_label(guess_message, self.colors['success'])
                return

        # If no planet exceeds the threshold, show the current top guess
        top_planet = max(probabilities, key=probabilities.get)
        top_prob = probabilities[top_planet]
        
        guess_message = f"Hmm... I'm leaning towards {top_planet} {planet_emojis[top_planet]} ({top_prob:.2%})"
        self.update_thinking_label(guess_message, self.colors['highlight'])


def main():
    root = tk.Tk()
    app = AstronomyExpertSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()