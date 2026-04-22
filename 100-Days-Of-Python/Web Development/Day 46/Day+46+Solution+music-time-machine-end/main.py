from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# -----------------------------
# 1. GET USER INPUT
# -----------------------------
date = input("Which year do you want to travel to? Type date in YYYY-MM-DD format: ")

# -----------------------------
# 2. SCRAPE BILLBOARD 100
# -----------------------------
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Accept-Language": "en-US,en;q=0.9"
}

billboard_url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url=billboard_url, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# -----------------------------
# 3. SPOTIFY AUTHENTICATION
# -----------------------------
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        redirect_uri="http://127.0.0.1:8888/callback",
        client_id="f160abacc43240bfb96296f288271db3",
        client_secret="95abc6eafa5b44439aabe79ca0b7484c",
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

# -----------------------------
# 4. SEARCH SONGS ON SPOTIFY
# -----------------------------
song_uris = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=song, type="track", limit=1)

    if result["tracks"]["items"]:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    else:
        print(f"❌ Not found on Spotify: {song}")

# -----------------------------
# 5. CREATE PLAYLIST
# -----------------------------
playlist = sp.current_user_playlist_create(
    name=f"{date} Billboard 100",
    public=False
)

print(f"✅ Playlist created: {playlist['name']}")

# -----------------------------
# 6. ADD SONGS TO PLAYLIST
# -----------------------------
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)

print("🎧 Songs successfully added to playlist!")
