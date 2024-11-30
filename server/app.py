from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Serve the favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

@app.route('/print/<string:input_string>')
def print_string(input_string):
    print(input_string)  # prints to the server's console
    return f"Printed: {input_string}"

@app.route('/count/<int:num>')
def count(num):
    return '<br>'.join(str(i) for i in range(1, num + 1))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == 'add':
        return str(num1 + num2)
    elif operation == 'subtract':
        return str(num1 - num2)
    elif operation == 'multiply':
        return str(num1 * num2)
    elif operation == 'divide':
        return str(num1 / num2 if num2 != 0 else 'Cannot divide by zero')
    elif operation == 'mod':
        return str(num1 % num2)
    else:
        return 'Invalid operation', 400

if __name__ == '__main__':
    app.run(debug=True)

