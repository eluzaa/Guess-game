from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Global variables to store the random number and attempts
rand_num = random.randrange(1, 50)
attempts = 0

@app.route('/', methods=['GET', 'POST'])
def guess_number():
    global rand_num, attempts
    message = ""
    
    if request.method == 'POST':
        user_guess = int(request.form['guess'])
        attempts += 1
        
        if user_guess < rand_num:
            message = "Selected number is higher than your guess..."
        elif user_guess > rand_num:
            message = "Selected number is lower than your guess..."
        else:
            message = f"Congrats! You've guessed the number after {attempts} tries!"
            rand_num = random.randrange(1, 50)  # Reset for the next game
            attempts = 0

    return render_template('index.html', message=message, attempts=attempts)

if __name__ == '__main__':
    app.run(debug=True)
