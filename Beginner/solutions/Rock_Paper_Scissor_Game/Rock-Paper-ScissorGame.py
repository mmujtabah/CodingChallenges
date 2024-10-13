import random

def play():
    moves = ["Rock", "Paper", "Scissors"]
    user_move = input("Enter your move (Rock, Paper, or Scissors): ").lower()
    if user_move not in moves:
        print("Invalid move! Please choose Rock, Paper, or Scissors.")
        return
    computer_move = random.choice(moves)
    print(f"\nYou chose: {user_move}")
    print(f"Computer chose: {computer_move}")
    if user_move == computer_move:
        print("It's a Tie!")
    elif (user_move == "Rock" and computer_move == "Scissors") or \
         (user_move == "Scissors" and computer_move == "Paper") or \
         (user_move == "Paper" and computer_move == "Rock"):
        print("You Win")
    else:
        print("You Lose")
play()
