import tkinter as tk
from tkinter import messagebox
import random


def play_game(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, result)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "User"
    else:
        return "Computer"


def display_result(user_choice, computer_choice, result):
    if result == "Draw":
        result_text = f"Both chose {user_choice}. It's a draw!"
    elif result == "User":
        result_text = f"You chose {user_choice}, Computer chose {computer_choice}. You win!"
    else:
        result_text = f"You chose {user_choice}, Computer chose {computer_choice}. You lose!"

    result_label.config(text=result_text)


# GUI Setup
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")
root.geometry("400x300")
root.configure(bg="#9516a6")

# User Name Entry
user_name_label = tk.Label(root, text="Enter your name:", bg="#9516a6")
user_name_label.pack()
user_name_entry = tk.Entry(root)
user_name_entry.pack()

# Level Selection
level_label = tk.Label(root, text="Select Level:", bg="#9516a6")
level_label.pack()
level_var = tk.StringVar(value="Easy")
level_easy = tk.Radiobutton(
    root, text="Easy", variable=level_var, value="Easy", bg="#9516a6")
level_easy.pack()
level_hard = tk.Radiobutton(
    root, text="Hard", variable=level_var, value="Hard", bg="#9516a6")
level_hard.pack()

# Choices Buttons
rock_button = tk.Button(
    root, text="Rock", command=lambda: play_game("Rock"), bg="#ff6666")
rock_button.pack(pady=5)

paper_button = tk.Button(
    root, text="Paper", command=lambda: play_game("Paper"), bg="#66ff66")
paper_button.pack(pady=5)

scissors_button = tk.Button(
    root, text="Scissors", command=lambda: play_game("Scissors"), bg="#6666ff")
scissors_button.pack(pady=5)

result_label = tk.Label(root, text="", bg="#9516a6", font=("Roboto", 12))
result_label.pack(pady=20)

root.mainloop()
