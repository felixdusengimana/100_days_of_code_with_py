from bs4 import BeautifulSoup
import requests
import html
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "7028fcb2f9454a10b45bcf7a8ef47b6a"
CLIENT_SECRET = "89cdb767f4ac4996b5f345e31e9cbff9"

BILLBOARD_ROOT_URL = "https://www.billboard.com/charts/hot-100/"

# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
date = "2000-08-12"
billboard_html = requests.get(BILLBOARD_ROOT_URL+date).text
soup = BeautifulSoup(billboard_html, 'html.parser')

song_name_h3s = soup.find_all("h3", class_="a-no-trucate", id="title-of-a-story")
song_names = [html.unescape(song.getText().strip()) for song in song_name_h3s]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()
print(user_id)

#Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

#Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)