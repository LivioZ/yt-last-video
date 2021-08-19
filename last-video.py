from googleapiclient.discovery import build
import json

# Channel ID
CHID = ''

# API Key
with open('key.json') as f:
    API_KEY = json.load(f)['key']


# Channel information
# request creation
youtube = build('youtube', 'v3', developerKey = API_KEY)

request = youtube.channels().list(
    part = 'contentDetails',
    id = CHID
)

response = request.execute()
# get the playlistId of the uploaded videos playlist
UPLOADS_ID = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

# last video
youtube = build('youtube', 'v3', developerKey = API_KEY)

request = youtube.playlistItems().list(
    part = 'snippet',
    playlistId = UPLOADS_ID,
    maxResults = 1
)

response = request.execute()
last_video_title = response['items'][0]['snippet']['title']
last_video_link = 'https://www.youtube.com/watch?v={}'.format(response['items'][0]['snippet']['resourceId']['videoId'])

print(last_video_title)
print(last_video_link)

youtube.close()
