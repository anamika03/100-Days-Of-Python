# # Function can have inputs/functionality/outputs
# def add(num1, num2):
#     return num1 + num2

# def subtract(num1, num2):
#     return num1 - num2

# def multiply(num1, num2):
#     return num1 * num2

# def divide(num1, num2):
#     if num2 == 0:
#         return "Cannot divide by zero"
#     return num1 / num2

# # Functions are first-class objects, can be passed around as arguments
# # e.g, int/string/float etc.

# def calculate(calc_function, num1, num2):
#     return calc_function(num1, num2)

# result = calculate(add, 10, 5)
# print(result)  # Output: 15

# Functions can be nested in other functions

# def outer_function():
#     print("This is the outer function")

#     def inner_function():
#         print("This is the inner function")

#     inner_function()

# outer_function()

# # Functions can also return from other functions
# def outer_function():

#     print("This is the outer function")

#     def nested_function():
#         print("This is the nested function")

#     return nested_function   # <-- no ()

# inner_function = outer_function()
# inner_function()

# Python Decorator Function
import time

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        # Do something after
        
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello!")

def say_greeting():
    print("Greetings!")

@delay_decorator
def say_goodbye():
    print("Goodbye!")

say_hello()
say_greeting()
say_goodbye()