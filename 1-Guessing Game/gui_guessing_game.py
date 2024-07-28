import tkinter as tk
from tkinter import messagebox
import random

class GuessingGameGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Guessing Game")

        self.label = tk.Label(self.window, text="Guess a number between 1 and 100", font=("Arial", 24))
        self.label.pack(pady=20)

        self.entry = tk.Entry(self.window, font=("Arial", 24))
        self.entry.pack(pady=20)

        self.button = tk.Button(self.window, text="Guess", command=self.check_guess, font=("Arial", 24))
        self.button.pack(pady=20)

        self.result_label = tk.Label(self.window, text="", font=("Arial", 24))
        self.result_label.pack(pady=20)

        self.number_to_guess = 42  # Replace with random number
        self.guesses = 0
        # Create menu
        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.window.bind("<Return>", self.check_guess)

        # Add "Game" menu
        self.game_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Game", menu=self.game_menu)
        self.game_menu.add_command(label="Play Again", command=self.play_again)
        self.game_menu.add_separator()
        self.game_menu.add_command(label="Exit", command=self.window.quit)

    def play_again(self):
        self.number_to_guess = random.randint(1, 100)
        self.guesses = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.button.config(state="normal")
    def check_guess(self, event = None):
        try:
            num = int(self.entry.get())
            self.guesses += 1
            if num == 0:
                messagebox.showinfo("Exit", "Exiting the program...")
                self.window.quit()
            elif self.number_to_guess == num:
                messagebox.showinfo("Congratulations", f"You guessed the correct number! It took you {self.guesses} attempts.")
                self.button.config(state="disabled")
            elif num > self.number_to_guess:
                self.result_label.config(text="Too high, guess a lower number.")
            else:
                self.result_label.config(text="Too low, guess a higher number.")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a number.")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui_game = GuessingGameGUI()
    gui_game.run()