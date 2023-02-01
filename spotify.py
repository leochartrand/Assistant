from spotipy.oauth2 import SpotifyOAuth
from spotipy import Spotify
import time
import os

auth_manager = SpotifyOAuth(
    client_id=os.getenv("SPOTIFY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://localhost:8080/",
    scope="user-read-private user-read-playback-state user-modify-playback-state user-read-currently-playing",
    username=os.getenv("SPOTIFY_USERNAME"))
spotify = Spotify(auth_manager=auth_manager)

deviceID = None
for d in spotify.devices()['devices']:
    if d['name'] == 'ubuntu':
        deviceID = d['id']
        break

state = "Waiting for request."

def get_state():
    return state

def get_current_track():
    time.sleep(2)
    context = spotify.current_user_playing_track()
    return "\033[32mCurrently playing: %s by %s\033[0m" % (context["item"]["name"], context["item"]["artists"][0]["name"])

def play_request(device_id=None, name: str=None, commandType=None):
    global state
    # Get URI
    query = name.replace(' ', '+')

    if commandType == 'track':
        group = 'tracks'
    elif commandType == 'album':
        group = 'albums'
    elif commandType == 'artist':
        group = 'artists'
    else:
        group = None

    searchResults = spotify.search(q=query, limit=1, type=commandType)
    if group == None:
        if not (searchResults['tracks']['items'] or searchResults['artists']['items'] or searchResults['albums']['items']):
            raise Exception(f'"{name}" was not found on Spotify')
        # should check for best type
        uri = searchResults['tracks']['items'][0]['uri']
    else:
        if not searchResults[group]['items']:
            raise Exception(f'No "{commandType}" named "{name}"')
        uri = searchResults[group]['items'][0]['uri']

    # Playback
    if commandType == 'artist' or commandType == 'album':
        spotify.start_playback(device_id=deviceID, context_uri=uri)
    else:
        spotify.start_playback(device_id=deviceID, uris=[uri])
    state = get_current_track()
    return True

def resume():
    global state
    spotify.start_playback(device_id=deviceID)
    state = get_current_track()
    return True

def pause():
    global state
    spotify.pause_playback(device_id=deviceID)
    state = "Spotify paused."
    return True

def next_track():
    global state
    spotify.next_track(device_id=deviceID)
    state = get_current_track()
    return True

def previous_track():
    global state
    spotify.previous_track(device_id=deviceID)
    state = get_current_track()
    return True
