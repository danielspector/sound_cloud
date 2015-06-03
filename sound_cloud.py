#!/usr/bin/env python

import soundcloud
import urllib
import sys
import os

reload(sys)
sys.setdefaultencoding("UTF-8")

CLIENT_ID = 'c73fb7771f05466a2bf445811b3bb60c'
ARTIST = sys.argv[1]
# create a client object with your app credentials
client = soundcloud.Client(client_id=CLIENT_ID)

user = client.get('/resolve', url='https://soundcloud.com/'+ARTIST)
user_id = str(user.id)
# fetch track to stream
tracks = client.get('/users/'+user_id+'/tracks')
track_nums = len(tracks)
print "about to start.... printing " + str(track_nums) + " songs"

current_path = os.getcwd()
downloads_path = current_path + "/downloads/"
artist_path = downloads_path + ARTIST + "/"
if not os.path.exists(downloads_path):
    os.makedirs(downloads_path)

if not os.path.exists(artist_path):
    os.makedirs(artist_path)

for track in tracks:
  track.title = track.title.replace("/","-")
  file_title = artist_path + str(user.username) + " - "+str(track.title)+".mp3"
  if os.path.isfile(file_title):
    print "Skipping" + file_title + " because it already exists"
    continue
  print "Downloading... " + str(track.title) + " by " + user.username
  try:
    stream_url = client.get(track.stream_url, allow_redirects=False)
    urllib.urlretrieve(stream_url.location, artist_path + str(user.username) + " - "+str(track.title)+".mp3")
    track_nums -= 1
    print str(track_nums) + " left to download"
  except:
    pass
print "done"

