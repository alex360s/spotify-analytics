import requests
from spotify_api import get_access_token

BASE_URL = "https://api.spotify.com/v1"


def get_artists_from_playlist(playlist_id: str, limit: int = 100):
    token = get_access_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }

    artists = {}

    url = f"{BASE_URL}/playlists/{playlist_id}/tracks"
    params = {
        "limit": 100
    }

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()

    items = response.json()["items"]

    for item in items:
        track = item["track"]
        if not track:
            continue

        for artist in track["artists"]:
            artist_id = artist["id"]
            if artist_id not in artists:
                artists[artist_id] = {
                    "id": artist_id,
                    "name": artist["name"]
                }

    return list(artists.values())
