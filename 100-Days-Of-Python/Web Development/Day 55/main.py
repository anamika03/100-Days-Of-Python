from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<name>/<int:age>')
def greet(name, age):
    return f'Hello, {name}! You are {age} years old.'

@app.route('/bye')
def bye():
    return 'Goodbye!'

if __name__ == '__main__':
    app.run(debug=True)

