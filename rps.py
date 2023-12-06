import tkinter as tk
from tkinter import ttk
import random

player_score = 0
computer_score = 0

def play_game(player_choice):
    global player_score, computer_score

    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)

    result = ""

    if player_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You win!"
        player_score += 1
    else:
        result = "Computer wins!"
        computer_score += 1

    result_label.config(text=f"Computer chose {computer_choice}. {result}")
    update_score()

def update_score():
    score_label.config(text=f"Player: {player_score}  |  Computer: {computer_score}")


root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Set the background color
root.configure(bg='#F7DC6F')

title_label = ttk.Label(root, text="Rock, Paper, Scissors", font=("Helvetica", 16), background='#F7DC6F')
title_label.pack(pady=10)

result_label = ttk.Label(root, text="", font=("Helvetica", 12), background='#F7DC6F')
result_label.pack(pady=20)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), background='#3498DB', foreground='#000000')

rock_button = ttk.Button(root, text="Rock", command=lambda: play_game("Rock"))
rock_button.pack(side=tk.LEFT, padx=10)

paper_button = ttk.Button(root, text="Paper", command=lambda: play_game("Paper"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = ttk.Button(root, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.pack(side=tk.LEFT, padx=10)

# label for the score (player and computers)
score_label = ttk.Label(root, text="Player: 0  |  Computer: 0", font=("Helvetica", 12), background='#F7DC6F')
score_label.pack(pady=10)


root.mainloop()
