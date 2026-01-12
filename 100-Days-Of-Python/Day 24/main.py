# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt") as file:    # automatically closes the file after the block and bydefault mode is 'r' for read.
    contents = file.read()
    print(contents)

with open("new_file.txt", mode="a") as file:  # 'a' mode is for append
    file.write("Ich bin Sechsundzwanzig Jahre alt.")


# Relative vs Absolute file paths
# absolute path: /Users/username/Documents/100_Days_of_Python/100-Days-Of-Python/Day 24/my_file.txt 
# #absolute path starts from root directory

# relative path: Day 24/my_file.txt 
# # relative to current working directory 



