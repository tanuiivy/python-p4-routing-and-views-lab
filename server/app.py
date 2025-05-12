#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Prints the string in the console
    return f'<h1>{param}</h1>'  # Displays the string in the browser

# Count route
@app.route('/count/<int:num>')
def count(num):
    result = ''.join([f'<p>{i}</p>' for i in range(1, num + 1)])
    return result

# Math operation route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return '<h1>Cannot divide by zero!</h1>'
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return f'<h1>Invalid operation: {operation}</h1>'

    return f'<h1>{num1} {operation} {num2} = {result}</h1>'

if __name__ == '__main__':
    app.run(port=5555, debug=True)

