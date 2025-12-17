from spotify_api import get_access_token, get_artist
ARTIST_IDS = [
    "5NMwoStnfHT4LdETlJSwDT",
    "2hTmpvdwhpNZryOkwTisRW",
    "5B5qmrbTFvA7TAxWruuwbo",
    "2z20q6EEfm6w6PiIKsgtb3",
    "76ZDdIwxzIsdzCAgf8gXaJ",
    "3vvLuXEEf7sl3izJcw0GIn",
    "6WI9EjCdJWcwOFFtubMrGM",
    "35m8HjyHmGQxAKfIBVHZpF",
    "5NipqMGsY4AUeb7kGT8aVz",
    "1Xyo4u8uXC1ZmMpatF05PJ",
    "5K4W6rqBFWDnAN6FQUkS6x",
    "0iEtIxbK0KxaSlF7G42ZOp",
    "2hlmm7s2ICUX0LVIhVFlZQ",
    "2YZyLoL8N0Wb9xBt1NhZWg",
    "0EmeFodog0BfCgMzAIvKQp",
    "5H4yInM5zmHqpKIoMNAx4r",
    "4h8pGxEIOi7j4me1yhYxlD",
    "6iQqWcDg92kre5ykFLwqD8",
    "5VxeSwDCDsUT35ggejgYo2",
    "0KaA8HctO3Rt7xjMSu3YUk",
    "27kGBCjiz5OXojkKX4xQ6R",
    "4AM93R2m6QIKGPWH6QILF3",
    "0KckNa5t57sjaIMY9ftPV9",
    "69v4ZOOomf1TNp59YYB1j7",
    "6L5bLEtpxwd0KOdOr3gtW4",
]

access_token = get_access_token()

for artist_id in ARTIST_IDS:
    try:
        data = get_artist(artist_id, access_token)
        print("-------")
        print(f'Name - {data["name"]}')
        print(f'Followers - {data["followers"]["total"]}')
        print(f'Popularity - {data["popularity"]}')
    except:
        print(f"Erorr with artist's id - {artist_id}: {e}")
