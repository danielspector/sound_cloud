import soundcloud
import urllib

CLIENT_ID = 'c73fb7771f05466a2bf445811b3bb60c'
ARTIST = 'deejaytrademark'
# create a client object with your app credentials
client = soundcloud.Client(client_id=CLIENT_ID)

user = client.get('/resolve', url='https://soundcloud.com/'+ARTIST)
user_id = str(user.id)
# fetch track to stream
tracks = client.get('/users/'+user_id+'/tracks')
track_nums = len(tracks)
print "about to start.... printing " + str(track_nums) + " songs"
for track in tracks:
  print "Downloading " + str(track.title)
  stream_url = client.get(track.stream_url, allow_redirects=False)
  urllib.urlretrieve(stream_url.location, "/Users/danielspector/projects/code/sound_cloud/downloads/"+str(user.username)+" - "+str(track.title)+".mp3")
  track_nums -= 1
  print str(track_nums) + " left to download"

print "done"


