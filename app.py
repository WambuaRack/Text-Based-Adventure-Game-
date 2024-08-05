from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        door_choice = request.form['door']
        if door_choice == '1':
            return redirect(url_for('result', outcome='win'))
        elif door_choice == '2':
            return redirect(url_for('result', outcome='lose'))
        else:
            return redirect(url_for('home', message='Invalid choice. Please select door 1 or 2.'))
    return render_template('home.html')

# Result page
@app.route('/result/<outcome>')
def result(outcome):
    if outcome == 'win':
        message = "You enter a room full of treasures! You win!"
    elif outcome == 'lose':
        message = "Oh no! You are trapped in a dungeon forever. Game over!"
    else:
        message = "Invalid outcome."
    return render_template('result.html', message=message)

# Error handling for invalid routes
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
