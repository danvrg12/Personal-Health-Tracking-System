# app.py
from flask import Flask, render_template, request, redirect, url_for, session

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here'

users = {
    'user1': 'pass1',
    'user2': 'pass2'
}

@app.route('/')
def home():
    """
    Renders the main page.
    If a user is logged in, it redirects them to the dashboard.
    Otherwise, it shows the login page.
    """
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html', title='Sign In')

@app.route('/login', methods=['POST'])
def login():
    """
    Handles the login form submission.
    Authenticates the user and sets a session cookie if successful.
    """
    username = request.form.get('username')
    password = request.form.get('password')

    # Simple authentication check against the in-memory users dictionary
    if username in users and users[username] == password:
        session['user_id'] = username
        return redirect(url_for('dashboard'))
    else:
        # If authentication fails, render the login page again with an error message
        error = 'Invalid username or password. Please try again.'
        return render_template('lab7.html', title='Sign In', error=error)

@app.route('/register')
def register():
    """
    Renders a placeholder page for user registration.
    """
    return render_template('lab7.html', title='Register', content='''
        <h2>Create a New Account</h2>
        <p>This is the registration page. The link from the sign-in page works!</p>
    ''')

@app.route('/dashboard')
def dashboard():
    """
    Renders the user dashboard.
    Requires the user to be logged in.
    """
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('lab7.html', title='Dashboard', content=f'''
        <h2>Hello, {session['user_id']}!</h2>
        <p>Welcome to your health tracker dashboard. Here you can see a summary of your health records and progress.</p>
    ''')

@app.route('/add_record')
def add_record():
    """
    Renders the page for adding a new health record.
    Requires the user to be logged in.
    """
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('lab7.html', title='Add Record', content='''
        <h2>Add a New Health Record</h2>
        <p>This page is where you would add new data like your blood pressure, weight, or activity level.</p>
    ''')

@app.route('/history')
def history():
    """
    Renders the page to view a history of health records.
    Requires the user to be logged in.
    """
    if 'user_id' not in session:
        return redirect(url_for('home'))
    return render_template('lab7.html', title='History', content='''
        <h2>Your Health History</h2>
        <p>This page will show a list or chart of all your past health records.</p>
    ''')

@app.route('/logout')
def logout():
    """
    Logs the user out by clearing the session and redirects to the home page.
    """
    session.pop('user_id', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Run the application in debug mode for development.
    app.run(debug=True)

