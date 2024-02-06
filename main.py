
# Import the necessary libraries
from flask import Flask, request, redirect, url_for, render_template

# Create the Flask application
app = Flask(__name__)

# Define the route for the main page
@app.route("/")
def index():
    """Main page with a form to get the visitor's name"""
    
    # Return the index.html template
    return render_template('index.html')


# Define the route for submitting the form
@app.route("/submit", methods=['POST'])
def submit():
    """Handle the form submission and redirect to the result page"""
    
    # Get the visitor's name from the form data
    visitor_name = request.form.get('visitor_name')
    
    # Redirect the visitor to the 'result' page with the name as a query parameter
    return redirect(url_for('result', visitor_name=visitor_name))


# Define the route for displaying the greeting
@app.route("/result")
def result():
    """Display the greeting message to the visitor"""
    
    # Get the visitor's name from the query parameters
    visitor_name = request.args.get('visitor_name')
    
    # Render the 'result.html' template with the name as a variable
    return render_template('result.html', visitor_name=visitor_name)


# Run the application
if __name__ == "__main__":
    app.run(debug=True)


This code fulfills all the requirements by creating the necessary routes, handling form submissions and displaying the greeting message to the visitor. It ensures proper variable referencing and follows Python syntax and conventions, making it a valid and functional Flask application.