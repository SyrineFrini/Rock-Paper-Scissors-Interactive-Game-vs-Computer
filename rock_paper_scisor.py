import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Function to get computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle user choice
def on_user_choice(user_choice):
    global wins, losses, ties
    highlight_user_choice(user_choice)
    computer_choice = get_computer_choice()
    highlight_computer_choice(computer_choice)
    result = determine_winner(user_choice, computer_choice)
    if result == "You win!":
        wins += 1
    elif result == "You lose!":
        losses += 1
    else:
        ties += 1
    update_score()
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Function to highlight computer's choice
def highlight_computer_choice(computer_choice):
    computer_rock_button.config(bg="white")
    computer_paper_button.config(bg="white")
    computer_scissors_button.config(bg="white")
    if computer_choice == "rock":
        computer_rock_button.config(bg="red")
    elif computer_choice == "paper":
        computer_paper_button.config(bg="red")
    elif computer_choice == "scissors":
        computer_scissors_button.config(bg="red")

# Function to highlight the user's choice
def highlight_user_choice(user_choice):
    user_rock_button.config(bg="white")
    user_paper_button.config(bg="white")
    user_scissors_button.config(bg="white")
    if user_choice == "rock":
        user_rock_button.config(bg="blue")
    elif user_choice == "paper":
        user_paper_button.config(bg="blue")
    elif user_choice == "scissors":
        user_scissors_button.config(bg="blue")

# Function to update the score display
def update_score():
    score_label.config(text=f"Wins: {wins}   Losses: {losses}   Ties: {ties}")

# Create the main window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(bg="white")
root.eval('tk::PlaceWindow . center')

# Get screen size and set window size proportionally
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = int(screen_width * 0.345)
window_height = int(screen_height * 0.66)

# Calculate position to center the window
position_right = int(screen_width/2 - window_width/2)
position_down = int(screen_height/2 - window_height/2)

# Set window size and position
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_down}")

# Initialize win/loss/tie counters
wins = 0
losses = 0
ties = 0

# Create score label
score_label = tk.Label(root, text=f"Wins: {wins}   Losses: {losses}   Ties: {ties} ", font=("Arial", 18), bg="white")
score_label.grid(row=0, column=0, columnspan=3, pady=10)

# Load images
rock_image = ImageTk.PhotoImage(Image.open("rock.jpg").resize((100, 100), Image.ANTIALIAS))
paper_image = ImageTk.PhotoImage(Image.open("paper.jpg").resize((100, 100), Image.ANTIALIAS))
scissors_image = ImageTk.PhotoImage(Image.open("scissors.jpg").resize((100, 100), Image.ANTIALIAS))

# Add "Computer's Choice" label
computer_choice_label = tk.Label(root, text="Computer's Choice:", font=("Arial", 16), bg="white")
computer_choice_label.grid(row=1, column=1, pady=10)

# Create computer's choice buttons
computer_rock_button = tk.Button(root, image=rock_image)
computer_paper_button = tk.Button(root, image=paper_image)
computer_scissors_button = tk.Button(root, image=scissors_image)

# Arrange computer's choice buttons
computer_rock_button.grid(row=2, column=0, padx=10, pady=10)
computer_paper_button.grid(row=2, column=1, padx=10, pady=10)
computer_scissors_button.grid(row=2, column=2, padx=10, pady=10)

# Add "VS" label
vs_label = tk.Label(root, text="VS", font=("Arial", 24), bg="white")
vs_label.grid(row=3, column=1, pady=10)

# Add "Your Choice" label
user_choice_label = tk.Label(root, text="Your Choice:", font=("Arial", 16), bg="white")
user_choice_label.grid(row=4, column=1, pady=10)

# Create user's choice buttons
user_rock_button = tk.Button(root, image=rock_image, command=lambda: on_user_choice("rock"))
user_paper_button = tk.Button(root, image=paper_image, command=lambda: on_user_choice("paper"))
user_scissors_button = tk.Button(root, image=scissors_image, command=lambda: on_user_choice("scissors"))

# Arrange user's choice buttons
user_rock_button.grid(row=5, column=0, padx=10, pady=10)
user_paper_button.grid(row=5, column=1, padx=10, pady=10)
user_scissors_button.grid(row=5, column=2, padx=10, pady=10)

# Add result label under user's choice buttons
result_label = tk.Label(root, text="", font=("Arial", 16), bg="white")
result_label.grid(row=6, column=0, columnspan=3, pady=10)

# Start the GUI event loop
root.mainloop()
