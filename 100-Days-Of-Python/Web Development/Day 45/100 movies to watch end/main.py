import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/bakeboard-hot-100/2026-04-18/"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

all_songs = soup.find_all("h3", class_="chart-entry__title")

song_titles = [song.get_text() for song in all_songs]

with open("songs.txt", "w") as file:
    for song in song_titles:
        file.write(f"{song}\n")

        


'''
FAQ: Empire's website has changed!

When this lesson was created, I used this URL for the project: 
URL = "https://www.empireonline.com/movies/features/best-movies-2/"

However, Empire has since changed their website. You can see this when you inspect the movie title elements. 
You'll see that the h3 with the class "title" is no longer there. 
To use exactly the same code as per the solution, we can use a cached version of the website from the Internet Archive's Wayback Machine.

'''