# Randomisation and Python Lists
# Random Module methods
# randint(a, b)
# Returns a random integer between a and b (both inclusive). This also raises a ValueError if a > b.

import random
import my_module  # imported my own module

print(my_module.pi)

random_int = random.randint(1, 10)
print(random_int)

random_float = random.random()
print(random_float)