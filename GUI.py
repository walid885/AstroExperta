import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

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
        
        # Configure styles
        self.setup_styles()
        
        # Configure the grid weight
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
            command=self.start_game
        )
        self.start_button.grid(row=0, column=1, padx=10)
        
        self.yes_button = ttk.Button(
            self.buttons_frame,
            text="Yes",
            style='Answer.TButton',
            command=self.yes_clicked,
            state="disabled"
        )
        self.yes_button.grid(row=0, column=0, padx=10)
        
        self.no_button = ttk.Button(
            self.buttons_frame,
            text="No",
            style='Answer.TButton',
            command=self.no_clicked,
            state="disabled"
        )
        self.no_button.grid(row=0, column=2, padx=10)
        
        # Progress Frame
        self.progress_frame = ttk.Frame(self.main_frame, style='Main.TFrame')
        self.progress_frame.grid(row=3, column=0, columnspan=2, pady=20)
        
        self.progress_label = ttk.Label(
            self.progress_frame,
            text="Progress: 0%",
            style='Progress.TLabel'
        )
        self.progress_label.pack()
        
        self.progress_bar = ttk.Progressbar(
            self.progress_frame,
            length=300,
            mode='determinate',
            style='Cosmic.Horizontal.TProgressbar'
        )
        self.progress_bar.pack(pady=10)
        
        # Game state variables
        self.game_active = False
        self.current_question = 0
    
    def setup_styles(self):
        """Configure custom styles for the application"""
        style = ttk.Style()
        
        # Configure frame styles
        style.configure('Main.TFrame', background=self.colors['bg_dark'])
        style.configure('Question.TLabelframe', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Question.TLabelframe.Label', 
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 12, 'bold'))
        
        # Configure label styles
        style.configure('Question.TLabel',
                       background=self.colors['bg_medium'],
                       foreground=self.colors['text'])
        style.configure('Progress.TLabel',
                       background=self.colors['bg_dark'],
                       foreground=self.colors['text'],
                       font=('Helvetica', 10))
        
        # Configure button styles
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
        
        # Configure progress bar style
        style.configure('Cosmic.Horizontal.TProgressbar',
                       troughcolor=self.colors['bg_medium'],
                       background=self.colors['accent'],
                       darkcolor=self.colors['accent'],
                       lightcolor=self.colors['highlight'])
    
    def start_game(self):
        self.game_active = True
        self.yes_button.config(state="normal")
        self.no_button.config(state="normal")
        self.start_button.config(state="disabled")
        self.question_label.config(text="✨ Is your celestial object a star?")
        self.progress_bar["value"] = 0
        self.update_progress()
    
    def yes_clicked(self):
        self.process_answer(True)
    
    def no_clicked(self):
        self.process_answer(False)
    
    def process_answer(self, answer):
        self.current_question += 1
        self.update_progress()
        
        if self.current_question >= 5:
            self.end_game()
        else:
            self.question_label.config(text=f"Question {self.current_question + 1}")
    
    def update_progress(self):
        progress = (self.current_question / 5) * 100
        self.progress_bar["value"] = progress
        self.progress_label.config(text=f"Cosmic Progress: {int(progress)}%")
    
    def end_game(self):
        messagebox.showinfo("Journey Complete", "Thank you for exploring the cosmos with us! 🌌")
        self.reset_game()
    
    def reset_game(self):
        self.game_active = False
        self.current_question = 0
        self.yes_button.config(state="disabled")
        self.no_button.config(state="disabled")
        self.start_button.config(state="normal")
        self.question_label.config(text="🌟 Think of a celestial object and press Start! 🌟")
        self.progress_bar["value"] = 0
        self.progress_label.config(text="Cosmic Progress: 0%")

def main():
    root = tk.Tk()
    app = AstronomyExpertSystem(root)
    root.mainloop()

if __name__ == "__main__":
    main()