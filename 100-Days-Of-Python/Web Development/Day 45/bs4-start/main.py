# Beautiful Soup is a Python library for pulling data out of HTML and XML files.
# It works with your favorite parser to provide idiomatic ways of navigating, searching and modifying the parse tree. 
# Beautiful Soup is often used for web scraping, which is the process of extracting data from websites.

from bs4 import BeautifulSoup
# import lxml

with open('/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Web Development/Day 45/bs4-start/website.html') as file:
    contents = file.read()

soup = BeautifulSoup(contents, 'html.parser')
print(soup.title)   # <title>Anamika's Personal Site</title>
print(soup.title.name)  # title
print(soup.title.string)    # Anamika's Personal Site
# print(soup.title.getText())  # Anamika's Personal Site
# print(soup.title.text)  # Anamika's Personal Site   

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.getText())    # LinkedIn
    print(tag.get("href"))  # https://www.linkedin.com/in/anamika-srivastava-9b1a5b1b3/

# print("\n", all_anchor_tags)


name = soup.find(name="h1", id="name")
print(name)

heading = soup.find(name="h3", class_="heading")
print(heading)

company_url = soup.select_one(selector="p a")
print(company_url)