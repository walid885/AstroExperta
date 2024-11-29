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
            command=self.start_game
        )
        self.start_button.grid(row=0, column=1, padx=10)
        
        self.yes_button = ttk.Button(
            self.buttons_frame,
            text="Yes",
            style='Answer.TButton',
            command=lambda: self.process_answer(True),
            state="disabled"
        )
        self.yes_button.grid(row=0, column=0, padx=10)
        
        self.no_button = ttk.Button(
            self.buttons_frame,
            text="No",
            style='Answer.TButton',
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



    def update_histogram(self):
        """Update the histogram on the canvas with current probabilities."""
        # Clear any existing widgets in the canvas frame
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        
        # Create a new figure with a specific size
        plt.figure(figsize=(8, 6), dpi=100, facecolor=self.colors['bg_medium'])
        
        # Convert probabilities to a DataFrame
        df = pd.DataFrame({
            'Celestial Object': list(self.expert_system.possible_planets.keys()),
            'Probability': list(self.expert_system.possible_planets.values())
        })
        
        # Set up the plot with a dark theme
        plt.style.use('dark_background')
        
        # Plot using seaborn with enhanced styling
        ax = sns.barplot(
            x='Celestial Object', 
            y='Probability', 
            data=df, 
            palette='viridis', 
            hue='Celestial Object', 
            dodge=False,
            legend=False
        )
        
        # Customizing the plot
        plt.title('Probability of Celestial Objects', 
                  color=self.colors['text'], 
                  fontsize=16, 
                  fontweight='bold')
        plt.xlabel('Celestial Objects', color=self.colors['text'])
        plt.ylabel('Probability', color=self.colors['text'])
        plt.xticks(rotation=45, color=self.colors['text'])
        plt.yticks(color=self.colors['text'])
        
        # Add value labels on top of each bar
        for i, v in enumerate(df['Probability']):
            ax.text(i, v, f'{v:.4f}', 
                    ha='center', va='bottom', 
                    color=self.colors['text'], 
                    fontweight='bold')
        
        plt.tight_layout()

        # Create canvas and embed plot in Tkinter
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(fill=tk.BOTH, expand=True)
        
        # Draw the canvas
        canvas.draw()
        
        # Close the figure to free up memory
        plt.close()

    def start_game(self):
        """Start the game by enabling buttons and fetching the first question."""
        self.expert_system.reset_game()
        question = self.expert_system.get_next_question()
        
        if question:
            question_id, question_text, feature_map = question
            self.current_question_id = question_id
            self.current_feature_map = feature_map

            self.question_label.config(text=question_text)
            self.start_button.config(state="disabled")
            self.yes_button.config(state="normal")
            self.no_button.config(state="normal")

            # Reset thinking label to initial state
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

            else:
                guess = self.expert_system.get_most_likely_planet()  
                messagebox.showinfo("Guess", f"I think it's {guess}!")  

                if guess == "Earth":
                    messagebox.showinfo("Correct Guess!", "Great! I guessed it right!")
                else:
                    messagebox.showinfo("Wrong Guess", f"I guessed {guess}, was I right?")

            # Update probabilities display after processing answer.
            self.update_probabilities_display()
            # Update histogram after processing answer.
            self.update_histogram()

    def update_probabilities_display(self):
        """Display current probabilities of each planet."""
        probabilities_text = "Current Probabilities:\n"
        for planet, prob in sorted(self.expert_system.possible_planets.items(), key=lambda x: x[1], reverse=True):
            probabilities_text += f"{planet}: {prob:.4f}\n"
        
        if max(self.expert_system.possible_planets.values()) > 0.8:
            guess_planet = max(self.expert_system.possible_planets.items(), key=lambda x: x[1])[0]
            probabilities_text += f"\nI might guess: {guess_planet}!"
        
        self.probability_label.config(text=probabilities_text)

def main():
    root = tk.Tk()
    app = AstronomyExpertSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()