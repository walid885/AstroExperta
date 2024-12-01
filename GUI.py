import tkinter as tk
from tkinter import ttk
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.font as tkFont

class SolarSystemExpertGUI:
    def __init__(self):
        self.reset_game()

    def reset_game(self):
        self.current_question = 0
        self.probabilities = {'Mercury': 0.125, 'Venus': 0.125, 'Earth': 0.125, 'Mars': 0.125,
                              'Jupiter': 0.125, 'Saturn': 0.125, 'Uranus': 0.125, 'Neptune': 0.125}
        self.feature_map = {}

    def get_next_question(self):
        questions = [
            ("Is it closer to the Sun than Earth?", "Mercury, Venus, Earth", {"Mercury": True, "Venus": True, "Earth": False}),
            ("Does it have rings?", "Saturn, Jupiter, Uranus, Neptune", {"Saturn": True, "Jupiter": False, "Uranus": True, "Neptune": True}),
            ("Is it the third planet from the Sun?", "Earth", {"Earth": True}),
            ("Does it have a solid surface?", "Mercury, Venus, Earth, Mars", {"Mercury": True, "Venus": True, "Earth": True, "Mars": True}),
        ]
        
        if self.current_question < len(questions):
            question, feature, feature_map = questions[self.current_question]
            self.feature_map = feature_map
            self.current_question += 1
            return question, feature, feature_map
        else:
            return None

    def update_probabilities(self, question_id, answer, feature_map):
        for planet, is_answered in feature_map.items():
            if is_answered == answer:
                self.probabilities[planet] += 0.25
            else:
                self.probabilities[planet] -= 0.25

    def get_most_likely_planet(self):
        return max(self.probabilities, key=self.probabilities.get)

    def get_probability_dataframe(self):
        return pd.DataFrame(list(self.probabilities.items()), columns=["Celestial Object", "Probability"])

class AstronomyExpertSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("AstroAcademy Expert System")

        # Set window size and allow resizing
        self.root.geometry("1200x700")
        self.root.minsize(1200, 700)
        self.root.configure(bg='#0B1026')  # Background color

        # Initialize expert system
        self.expert_system = SolarSystemExpertGUI()

        # Main container frame
        self.container = ttk.Frame(self.root)
        self.container.grid(row=0, column=0, sticky="nsew")

        # Configure grid responsiveness
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_columnconfigure(1, weight=1)
        self.container.grid_columnconfigure(2, weight=1)

        # Styles configuration
        self.setup_styles()

        # Title Label
        title_font = tkFont.Font(family="Helvetica", size=24, weight="bold")
        self.title_label = tk.Label(
            self.container,
            text="✧ AstroAcademy Expert System ✧",
            font=title_font,
            bg="#0B1026",
            fg="#E6E8F0"
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=20, sticky="n")

        # Visualization Frame (Left)
        self.visualization_frame = ttk.LabelFrame(
            self.container,
            text="Probability Visualization",
            padding="10"
        )
        self.visualization_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.visualization_frame.grid_rowconfigure(0, weight=1)
        self.visualization_frame.grid_columnconfigure(0, weight=1)
        self.canvas_frame = ttk.Frame(self.visualization_frame)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        # Question Frame (Middle)
        self.question_frame = ttk.LabelFrame(
            self.container,
            text="Your Cosmic Quest",
            padding="10"
        )
        self.question_frame.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        self.question_frame.grid_rowconfigure(0, weight=1)
        self.question_label = ttk.Label(
            self.question_frame,
            text="🌟 Think of a celestial object and press Start! 🌟",
            font=("Helvetica", 16),
            wraplength=350
        )
        self.question_label.pack(pady=20, expand=True)

        # Buttons Frame
        self.buttons_frame = ttk.Frame(self.question_frame)
        self.buttons_frame.pack(pady=10)
        self.start_button = ttk.Button(self.buttons_frame, text="Start Journey", command=self.start_game)
        self.start_button.grid(row=0, column=1, padx=5)
        self.yes_button = ttk.Button(self.buttons_frame, text="Yes", command=lambda: self.process_answer(True), state="disabled")
        self.yes_button.grid(row=0, column=0, padx=5)
        self.no_button = ttk.Button(self.buttons_frame, text="No", command=lambda: self.process_answer(False), state="disabled")
        self.no_button.grid(row=0, column=2, padx=5)
        self.reset_button = ttk.Button(self.buttons_frame, text="Reset Game", command=self.reset_game, state="disabled")
        self.reset_button.grid(row=1, column=1, padx=5, pady=(10, 0))

        # Thinking Frame (Right)
        self.thinking_frame = ttk.LabelFrame(
            self.container,
            text="System's Thought Process",
            padding="10"
        )
        self.thinking_frame.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.thinking_frame.grid_rowconfigure(0, weight=1)
        self.thinking_label = ttk.Label(
            self.thinking_frame,
            text="🤔 THINKING... 🌌",
            font=("Helvetica", 16, "bold")
        )
        self.thinking_label.pack(pady=20, expand=True)
        self.probability_label = ttk.Label(self.thinking_frame, text="Current Probabilities:")
        self.probability_label.pack(pady=10)

        # Initialize histogram
        self.initialize_histogram()

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("default")  # Use a default theme
        style.configure("TLabelFrame", background="#1B2559", foreground="#E6E8F0", relief="ridge")
        style.configure("TLabelFrame.Label", background="#1B2559", foreground="#E6E8F0")
        style.configure("TButton", background="#4B61D1", foreground="#E6E8F0", padding=5)
        style.configure("TLabel", background="#1B2559", foreground="#E6E8F0")

    def initialize_histogram(self):
        fixed_objects = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
        probabilities = [0.125] * len(fixed_objects)
        df = pd.DataFrame({'Celestial Object': fixed_objects, 'Probability': probabilities})
        self.create_histogram(df)

    def create_histogram(self, df):
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        plt.figure(figsize=(5, 4))
        sns.barplot(x='Celestial Object', y='Probability', data=df, palette='viridis')
        plt.title('Probability of Celestial Objects')
        plt.xlabel('Celestial Objects')
        plt.ylabel('Probability')
        plt.tight_layout()
        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        canvas.draw()

    def start_game(self):
        self.expert_system.reset_game()
        self.initialize_histogram()
        question = self.expert_system.get_next_question()
        if question:
            question_text, feature, feature_map = question
            self.current_question_text = question_text
            self.current_feature_map = feature_map
            self.question_label.config(text=question_text)
            self.yes_button.config(state="normal")
            self.no_button.config(state="normal")
            self.start_button.config(state="disabled")
            self.reset_button.config(state="normal")
            self.thinking_label.config(text="🤔 THINKING... 🌌")
        else:
            self.thinking_label.config(text="🤔 No questions available!")

    def process_answer(self, answer):
        self.expert_system.update_probabilities(self.current_question_text, answer, self.current_feature_map)
        next_question = self.expert_system.get_next_question()
        if next_question:
            question_text, feature, feature_map = next_question
            self.current_question_text = question_text
            self.current_feature_map = feature_map
            self.question_label.config(text=question_text)
        else:
            guess = self.expert_system.get_most_likely_planet()
            self.thinking_label.config(text=f"🤩 Is it {guess}?")
            self.yes_button.config(state="disabled")
            self.no_button.config(state="disabled")
        self.update_histogram()

    def update_histogram(self):
        self.create_histogram(self.expert_system.get_probability_dataframe())

    def reset_game(self):
        self.expert_system.reset_game()
        self.initialize_histogram()
        self.start_button.config(state="normal")
        self.yes_button.config(state="disabled")
        self.no_button.config(state="disabled")
        self.reset_button.config(state="disabled")
        self.question_label.config(text="🌟 Think of a celestial object and press Start! 🌟")
        self.thinking_label.config(text="🤔 THINKING... 🌌")

if __name__ == "__main__":
    root = tk.Tk()
    app = AstronomyExpertSystem(root)
    root.mainloop()
