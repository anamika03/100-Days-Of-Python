import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year, month, day = date.split("-")
print(f"You want to travel to the year {year}, month {month} and day {day}.")



URL = f"https://appbrewery.github.io/bakeboard-hot-100/{year}-{month}-{day}/"

response = requests.get(url=URL)
soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("h3", class_="chart-entry__title")

song_names = [song.getText().strip() for song in song_names_spans]

with open("song_files.txt", "w") as file:
    for song in song_names:
        file.write(f"{song}\n")

