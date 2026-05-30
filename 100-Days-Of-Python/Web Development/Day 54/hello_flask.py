from flask import Flask

app = Flask(__name__)   # __name__ is a special attribute in Python that represents the name of the current module. Flask uses this to determine the root path of the application.

@app.route('/')   # This decorator tells Flask that the function below it should be called when the root URL ("/") is accessed.
def hello_world():
    return 'Hello, World!'

@app.route('/bye')   # This decorator tells Flask that the function below it should be called when the "/bye" URL is accessed.
def say_bye():
    return 'Bye!'

if __name__ == '__main__':
    app.run()
