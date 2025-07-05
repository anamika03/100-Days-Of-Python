# 1. Describe the error.
# 2. Reproduce the Bug.

from random import randint
dice_images = ["1","2","3","4","5","6"]
# dice_num = randint(1, 6) when the value 6 comes it shows an error because list start from index 0 and goes till 6-1= 5 thats why it shows an error.
dice_num = randint(0, 5)
print(dice_images[dice_num])

