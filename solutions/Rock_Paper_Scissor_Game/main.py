from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Game Logic
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    computer_choice = ''
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
    
    return render_template('index.html', result=result, computer_choice=computer_choice)

if __name__ == '__main__':
    app.run(debug=True)
