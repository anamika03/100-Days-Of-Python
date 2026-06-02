# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return '<h1 style="text-align: center">Hello, World!</h1>' \
#            '<p>This is a simple Flask application.</p>' \
#            '<img src="https://www.python.org/static/community_logos/python-logo.png" alt="Python Logo">'

# def make_bold(func):
#     def wrapper():
#         return f'<b>{func()}</b>'
#     return wrapper

# def make_emphasis(func):
#     def wrapper():
#         return f'<em>{func()}</em>'
#     return wrapper

# def make_underlined(func):
#     def wrapper():
#         return f'<u>{func()}</u>'
#     return wrapper

# @app.route('/<name>/<int:age>')
# def greet(name, age):
#     return f'Hello, {name}! You are {age} years old.'

# @app.route('/bye')
# @make_bold
# @make_emphasis
# @make_underlined
# def bye():
#     return '<b>Goodbye!</b>'

# if __name__ == '__main__':
#     app.run(debug=True)

## Advance Python Decorator Functions

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(func):
    def wrapper(*args, **kwargs):
        if args and hasattr(args[0], 'is_logged_in') and args[0].is_logged_in:
            return func(*args, **kwargs)
        else:
            return 'You must be logged in to perform this action.'
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
    

new_user = User('Anamika')
new_user.is_logged_in = True
create_blog_post(new_user)