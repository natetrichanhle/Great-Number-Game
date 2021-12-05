from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
import random
# Create a new instance of the Flask class called "app"
app = Flask(__name__)
app.secret_key = "bofa"


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def index():
    guess_num = random.randint(1,100)
    if 'guess' not in session:
        session['guess'] = guess_num
    return render_template('index.html')

@app.post('/guess')
def guess():
    input = int(request.form['input'])
    guess = session['guess']
    if input == guess:
        return 'Correct!'
    if input > guess:
        return 'Too high!'
    if input < guess:
        return 'Too low!'
    return redirect('/')

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.
