import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont
from Expert_System.knlowledge_engineGUIntegr import SolarSystemExpertGUI  # Importing the expert system

class AstronomyExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("AstroAcademy Expert System")
        self.root.geometry("800x600")
        
        # Color scheme
        self.colors = {
            'bg_dark': '#0B1026',      # Deep space blue
            'bg_medium': '#1B2559',    # Midnight blue
            'accent': '#4B61D1',       # Stellar blue
            'text': '#E6E8F0',         # Starlight white
            'highlight': '#8B9EF0'     # Nebula purple
        }
        
        # Configure the root window
        self.root.configure(bg=self.colors['bg_dark'])
        
        # Initialize the expert system
        self.expert_system = SolarSystemExpertGUI()
        
        # Configure styles
        self.setup_styles()
        
        # Configure grid weight
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create main frame
        self.main_frame = ttk.Frame(self.root, style='Main.TFrame', padding="20")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Title Label with custom font
        title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(
            self.main_frame,
            text="✧ AstroAcademy Expert System ✧",
            font=title_font,
            bg=self.colors['bg_dark'],
            fg=self.colors['text']
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=30)
        
        # Question Frame
        self.question_frame = ttk.LabelFrame(
            self.main_frame,
            text="Your Cosmic Quest",
            style='Question.TLabelframe',
            padding="20"
        )
        self.question_frame.grid(row=1, column=0, columnspan=2, sticky="ew", pady=20, padx=20)
        
        # Question Label
        self.question_label = ttk.Label(
            self.question_frame,
            text="🌟 Think of a celestial object and press Start! 🌟",
            style='Question.TLabel',
            font=("Helvetica", 14)
        )
        self.question_label.pack(pady=15)
        
        # Buttons Frame
        self.buttons_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.buttons_frame.grid(row=2, column=0, columnspan=2, pady=30)
        
        # Custom button styles for each button type
        self.start_button = ttk.Button(
            self.buttons_frame,
            text="Start Journey",
            style='Start.TButton',
            command=self.start_game  # Start game method to fetch questions
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
        
        # Progress Frame (optional if you want to show progress)
        self.progress_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.progress_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.progress_label = ttk.Label(
            self.progress_frame,
            text="Progress: 0%",
            style='Progress.TLabel'
        )
        self.progress_label.pack()
        
    def setup_styles(self):
       """Configure custom styles for the application"""
       style = ttk.Style()
       style.configure('Main.TFrame', background=self.colors['bg_dark'])
       style.configure('Question.TLabelframe', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
       style.configure('Question.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
       style.configure('Start.TButton',
                       background=self.colors['accent'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 11, 'bold'),
                       padding=10)
       style.configure('Answer.TButton',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 11),
                       padding=10)

    def start_game(self):
       """Start the game by enabling buttons and fetching the first question."""
       self.expert_system.reset_game()  # Reset or initialize game state if needed
       question = self.expert_system.get_next_question()
       
       if question:
           question_id, question_text, _ = question  # Unpack question details
           self.question_label.config(text=question_text)  # Display question text
           self.start_button.config(state="disabled")  # Disable start button during questioning
           self.yes_button.config(state="normal")  # Enable yes/no buttons
           self.no_button.config(state="normal")

    def process_answer(self, answer):
       """Process user answers and update game state."""
       question_id = ...  # Retrieve current question ID (you may need to store this when fetching questions)
       
       if answer:
           response_text = "Great! Let's explore more."
           print("User answered Yes.")
       else:
           response_text = "Interesting! Let's see what else we can find."
           print("User answered No.")
       
       # Update probabilities in expert system based on user answer
       self.expert_system.process_answer(question_id, answer)

       next_question = self.expert_system.get_next_question()
       
       if next_question:
           question_id, question_text, _ = next_question  # Unpack next question details
           self.question_label.config(text=question_text)  # Update label with new question text
           print(f"Next Question: {question_text}")
           # Optionally update progress here if needed

       else:
           guess = self.expert_system.get_most_likely_planet()  # Get guess from expert system
           messagebox.showinfo("Guess", f"I think it's {guess}!")  # Display guess message

def main():
    root = tk.Tk()
    app = AstronomyExpertSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()