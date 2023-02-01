import listener
import speechToText
import textToCode
import spotify
import os

clear = lambda: os.system('clear')
clear()

def main():
    try:
        listener.listen()
        prompt = speechToText.transcribe()
        clear()
        print("%s" % prompt[1:])
        command = textToCode.transcribe(prompt)
        state = ""
        success = True

        if command == "There was an error transcribing to code.":
            print(command)
        elif command[0] == "SPOTIFY_ARTIST":
            spotify.play_request(name=command[1][0], commandType="artist")
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_ALBUM":
            spotify.play_request(name=command[1][0], commandType="album")
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_SONG":
            query = ""
            if type(command[1]) is list:
                for arg in command[1]:
                    query += arg + "+"
            else:
                query = command[1]
            spotify.play_request(name=query, commandType="track")
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_PLAYLIST":
            spotify.play_request(name=command[1][0], commandType="artist")
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_START_PLAYBACK":
            spotify.resume()
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_PAUSE_PLAYBACK":
            spotify.pause()
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_NEXT":
            spotify.next_track()
            state = spotify.get_state()
        elif command[0] == "SPOTIFY_PREVIOUS":
            spotify.previous_track()
            state = spotify.get_state()
        # Possibly upcoming features
        elif command[0] == "NETFLIX_MOVIE":
            pass
        elif command[0] == "NETFLIX_TV":
            pass
        elif command[0] == "BEDROOM_LIGHTS_ON":
            state = "Lights on!"
        elif command[0] == "BEDROOM_LIGHTS_OFF":
             state = "Lights off!"
        elif command[0] == "WEATHER_WIDGET":
            pass

        clear()
        print(state)

        return success

    except Exception as e:
        # print("Exception: " + str(e))
        return False
