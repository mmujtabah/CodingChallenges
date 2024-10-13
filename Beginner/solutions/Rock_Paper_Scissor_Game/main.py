from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Game Logic
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        session['wins'] += 1
        return "You win!"
    else:
        session['losses'] += 1
        return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'wins' not in session:
        session['wins'] = 0
        session['losses'] = 0
        session['ties'] = 0
    
    result = ''
    computer_choice = ''
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
    
    return render_template('index.html', result=result, computer_choice=computer_choice, score={'wins': session['wins'], 'losses': session['losses'], 'ties': session['ties']})

if __name__ == '__main__':
    app.run(debug=True)
