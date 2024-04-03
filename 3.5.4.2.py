import requests
import json

client_id = 'efb8b87150c8f3c0c06a'
client_secret = '598d7b96dc4a640c07030a1e17f4caa8'

r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })
j = json.loads(r.text)
token = j["token"]

artists = []

with open('C:/Users/tanze/Documents/Python/datten/dataset_24476_4.txt') as file:
    for artist_id in file:
        artist_id = artist_id.strip()
        url = 'https://api.artsy.net/api/artists/{artist_id}'
        params = {'xapp_token': token}
        resp = requests.get(url, params=params).text
        data = json.loads(resp)
        artists.append({'name': data['sortable_name'], 'birthday': data['birthday']})

for artist in sorted(artists, key=lambda x: (x['birthday'], x['name'])):
    print(artist['name'])