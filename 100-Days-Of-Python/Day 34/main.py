age: int
name: str
height: float
is_human: bool

def police_check(age: int) -> bool:
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive



if police_check(19):
    print("You can drive")
else:    
    print("You cannot drive")  


#Type Hinting is a way to indicate the expected data type of a variable, 
# function parameter, or return value. It helps improve code 
# readability and can assist with debugging and static analysis. 
# In the example above, we have defined variables with specific 
# data types (int, str, float, bool) and a function that takes an integer 
# as input and returns a boolean value.