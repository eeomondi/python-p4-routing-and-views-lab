from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:text>')
def print_string(text):
    print(text)  # Prints to the console
    return f'<p>{text}</p>'

@app.route('/count/<int:number>')
def count(number):
    return '<br>'.join(str(i) for i in range(1, number + 1))

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2 if num2 != 0 else "Error: Division by zero"
    elif operation == '%':
        result = num1 % num2
    else:
        return f"Operation {operation} not supported"
    
    return f'{num1} {operation} {num2} = {result}'

if __name__ == '__main__':
    app.run(debug=True)

