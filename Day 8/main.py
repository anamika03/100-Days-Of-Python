#FUNCTION
#  name     =    Krishan
#    |              |
# parameter      argument


# def greet(name):  #parameter
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#     print("Bye, see you soon!")

# greet("Krishan")  #argument passed

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

#Positional Arguments
greet_with("Anamika", "Nowhere") 
greet_with("Nowhere", "Anamika") 
# greet_with("Anamika")  #TypeError: greet_with() missing 1 required positional argument: 'location'

# Keyword Arguments
greet_with(location = "London", name = "Anamika") 