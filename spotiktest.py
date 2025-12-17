import requests
import base64
CLIENT_ID = ""
CLIENT_SECRET = ""
auth_string = f"{CLIENT_ID}:{CLIENT_SECRET}"
auth_bytes = auth_string.encode("utf-8")
auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")


token_url = "https://accounts.spotify.com/api/token"
headers = {
    "Authorization": f"Basic {auth_base64}"
}
data = {
    "grant_type": "client_credentials"
}

response = requests.post(token_url, headers=headers, data=data)
access_token = response.json()["access_token"]

print("TOKEN OK")

# 2. Запрос артиста (например Drake)
artist_id = "69v4ZOOomf1TNp59YYB1j7"
artist_url = f"https://api.spotify.com/v1/artists/{artist_id}"

headers = {
    "Authorization": f"Bearer {access_token}"
}

artist_response = requests.get(artist_url, headers=headers)
artist_data = artist_response.json()

print("Artist:", artist_data["name"])
print("Genres:", artist_data["genres"])
print("Popularity:", artist_data["popularity"])
print("Followers:", artist_data["followers"]["total"])