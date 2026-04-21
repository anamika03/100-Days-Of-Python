# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# It works with your favorite parser to provide idiomatic ways of navigating, searching and modifying the parse tree. 
# Beautiful Soup is often used for web scraping, which is the process of extracting data from websites.

from bs4 import BeautifulSoup
# import lxml

with open('website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title.string)


