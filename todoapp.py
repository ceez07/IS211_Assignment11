# Import required Flask tools
from flask import Flask, render_template, request, redirect

# Import regex for email validation
import re

# Create Flask app
app = Flask(__name__)

# This will store all To-Do items (global list)
todo_list = []



# MAIN PAGE ROUTE (/)

@app.route('/')
def index():
    # Renders the HTML page and sends the list of todos to it
    return render_template('index.html', todos=todo_list)


# SUBMIT ROUTE (/submit)
@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form inputs
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # EMAIL VALIDATION
    # Check if email format is valid using regex
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        # If invalid, send user back to main page
        return redirect('/')

    # PRIORITY VALIDATION
    # Make sure priority is one of the allowed values
    if priority not in ['Low', 'Medium', 'High']:
        return redirect('/')

    # ADD ITEM TO LIST
    # Create a dictionary for the new To-Do item
    new_item = {
        "task": task,
        "email": email,
        "priority": priority
    }

    # Add it to the global list
    todo_list.append(new_item)

    # Redirect back to main page to show updated list
    return redirect('/')


# CLEAR ROUTE (/clear)
@app.route('/clear', methods=['POST'])
def clear():
    # Remove all items from the list
    todo_list.clear()

    # Redirect back to main page
    return redirect('/')


# RUN APP

if __name__ == '__main__':
    # Run Flask app in debug mode
    app.run(debug=True)