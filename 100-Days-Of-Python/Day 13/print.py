# 5. Print is your friend
# Squash bug with a print() statement

pages = int(input("Number of pages: "))
# print(f"pages: {pages}")

# word_per_page == int(input("Number of words per page: "))  # here is a bug: == 
word_per_page = int(input("Number of words per page: ")) 
# print(f"words per page: {word_per_page}")

total_words = pages * word_per_page
print(f"Total Words: {total_words}")
