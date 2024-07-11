import tkinter as tk
from tkinter import messagebox
import random
def play(choice):
    userchoice = choice
    comp_choice = random.choice(["rock", "paper", "scissors"])
    result = winner(userchoice, comp_choice)
    userlabel.config(text = f"You chose: {userchoice.capitalize()}")
    comp_label.config(text = f"Computer Chose: {comp_choice.capitalize()}")
    resultlabel.config(text = result)
    global userscore, comp_score
    if "Win" in result:
        userscore = userscore + 1
    elif "Lost" in result:
        comp_score += 1
    scorelabel.config(text = f"Scores - You: {userscore}, Computer: {comp_score}")
def winner(userchoice, comp_choice):
    if(userchoice == comp_choice):
        return "It is a TIE !"
    elif(userchoice == "rock" and comp_choice == "scissors") or \
        (userchoice == "scissors" and comp_choice == "paper") or \
        (userchoice == "paper" and comp_choice == "rock"):
            return "You Win !"
    else:
        return "You Lost!"
def play_again():
    userlabel.config(text= "")
    comp_label.config(text= "")
    resultlabel.config(text = "")
    global userscore, comp_score
    userscore, comp_score = 0, 0
    scorelabel.config(text= f"Scores - You: {userscore}, Computer: {comp_score}")
userscore = 0
comp_score = 0
root = tk.Tk()
root.title("Rock-Paper-Scissor-GAME")
rockbutton = tk.Button(root, text = "Rock", command = lambda: play("rock"))
rockbutton.pack(pady = 10)
paperbutton = tk.Button(root, text = "Paper", command = lambda: play("paper"))
paperbutton.pack(pady = 10)
scissorsbutton = tk.Button(root, text = "Scissors", command = lambda: play("scissors"))
scissorsbutton.pack(pady = 10)

userlabel = tk.Label(root, text = "")
userlabel.pack(pady = 10)
comp_label = tk.Label(root, text = "")
comp_label.pack(pady= 10)
resultlabel= tk.Label(root, text = "")
resultlabel.pack(pady = 10)
scorelabel = tk.Label(root, text= f"Scores - You: {userscore}, Computer: {comp_score}")
scorelabel.pack(pady= 10)
playagain_button= tk.Button(root, text = "Play Again", command = play_again)
playagain_button.pack(pady = 20)
root.mainloop()
        