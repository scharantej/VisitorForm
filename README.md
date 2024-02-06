## Design for Visitor's Name Form

---

## HTML Files

### 1. index.html:
- Purpose: This is the main HTML page of the website, welcoming the visitor and presenting them with the form to input their name.


### Content:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Visitor's Name Form</title>
</head>
<body>
  <h1>Welcome! Please enter your name:</h1>
  <form action="/submit" method="POST">
    <input type="text" name="visitor_name">
    <input type="submit" value="Submit">
  </form>
</body>
</html>
```


### 2. result.html:
- Purpose: This HTML page will display a greeting message to the visitor, using the input name from the form.


### Content:
```html
<!DOCTYPE html>
<html>
<head>
  <title>Hello, Visitor!</title>
</head>
<body>
  <h1>Hello, {{ visitor_name }}! Welcome to our website.</h1>
</body>
</html>
```

---

## Routes

### 1. Route for Form Submission - /submit:
- Method: POST
- Purpose: This route handles the form submission and captures the input visitor's name.


### Code: 
```python
@app.route("/submit", methods=['POST'])
def submit():
  # Get the visitor's name from the form data
  visitor_name = request.form.get('visitor_name')
  
  # Redirect the visitor to the 'result' page with the name as a query parameter
  return redirect(url_for('result', visitor_name=visitor_name))
```


### 2. Route for Displaying Greeting - /result:
- Method: GET
- Purpose: This route displays the greeting message to the visitor based on the name provided in the 'visitor_name' query parameter.


### Code: 
```python
@app.route("/result")
def result():
  # Get the visitor's name from the query parameters
  visitor_name = request.args.get('visitor_name')
  
  # Render the 'result.html' template with the name as a variable
  return render_template('result.html', visitor_name=visitor_name)
```