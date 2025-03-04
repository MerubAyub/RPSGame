from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # HTML file load hogi

if __name__ == '__main__':
    app.run(debug=True)

import random
# choices 
choices = ["rock", "paper", "scissors"]
player_name = input("Enter Your Name:")
# name == player_name
# player's choice
player_choice = input("Select One of Them (rock, paper, scissors):").lower()
# computer's choice
computer_choice = random.choice(choices)

# winner decision
if player_choice == computer_choice:
    print(f"Both Choose {player_choice}. It's a TIE!")
    
elif player_choice == "rock" and computer_choice == "scisssors":
    print(f"{player_name} WINS! {player_choice} beats {computer_choice}")
    
elif player_choice == "paper" and computer_choice == "rock":
    print(f"{player_name} WINS! {player_choice} beats {computer_choice}")
    
    play_again = input("Play Again? (y/n) ")
