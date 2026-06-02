from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a simple Flask application.</p>' \
           '<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">'


@app.route('/<name>/<int:age>')
def greet(name, age):
    return f'Hello, {name}! You are {age} years old.'

@app.route('/bye')
def bye():
    return 'Goodbye!'

if __name__ == '__main__':
    app.run(debug=True)

