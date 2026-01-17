def add(*args):    # args is a tuple
    print(args[0]) # first item
    print(args[-1]) # last item

    sum = 0
    for n in args:
        sum += n
    return sum

print(add(3,5,7,9,1,2,4,6,8,10))

def calculate(n, **kwargs):  # kwargs is a dictionary
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n   

print(calculate(2, add=3, multiply=5))

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.year = kw.get("year")
        self.color = kw.get("color")
        self.price = kw.get("price")
        self.mileage = kw.get("mileage")
        self.sunroof = kw.get("sunroof")
        self.navigation = kw.get("navigation")


my_car = Car(make="Ford", model="Mustang", year=2021, color="Red", price=30000, sunroof=True, navigation=True)
print(my_car.model)
my_other_car = Car()  # Create a car with no attributes
print(my_other_car.model)  # Should print None