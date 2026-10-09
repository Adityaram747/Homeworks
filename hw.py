import random
from tkinter import *


def play(user_choice):
    # Computer chooses randomly
    comp_choice = random.choice(["Rock", "Paper", "Scissors"])

    # Determine winner
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and comp_choice == "Scissors")
        or (user_choice == "Paper" and comp_choice == "Rock")
        or (user_choice == "Scissors" and comp_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    # Show choices and result in the label
    result_label.config(
        text=f"Your choice: {user_choice}\nComputer choice: {comp_choice}\n\n{result}"
    )


# --- GUI Setup ---
root = Tk()
root.title("Rock Paper Scissors")
root.geometry("350x250")
root.configure(bg="light blue")

# Title
title_label = Label(
    root,
    text="Rock Paper Scissors Game",
    font=("Helvetica", 14, "bold"),
    bg="light blue",
)
title_label.pack(pady=10)

# Buttons Frame
btn_frame = Frame(root, bg="light blue")
btn_frame.pack(pady=10)

Button(
    btn_frame,
    text="Rock",
    width=8,
    bg="white",
    command=lambda: play("Rock"),
).grid(row=0, column=0, padx=5)
Button(
    btn_frame,
    text="Paper",
    width=8,
    bg="white",
    command=lambda: play("Paper"),
).grid(row=0, column=1, padx=5)
Button(
    btn_frame,
    text="Scissors",
    width=8,
    bg="white",
    command=lambda: play("Scissors"),
).grid(row=0, column=2, padx=5)

# Result Output
result_label = Label(
    root,
    text="Click any button to play!",
    font=("Helvetica", 11),
    bg="light blue",
)
result_label.pack(pady=15)

root.mainloop()