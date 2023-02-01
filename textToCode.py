import os
import openai
import ast

openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe(command):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Return correct action. Prompt:\"%s\"\nActions are contained in this list: [\"SPOTIFY_ARTIST\", \"SPOTIFY_ALBUM\", \"SPOTIFY_SONG\", \"SPOTIFY_PLAYLIST\", \"SPOTIFY_START_PLAYBACK\", \"SPOTIFY_PAUSE_PLAYBACK\", \"SPOTIFY_NEXT\", \"SPOTIFY_PREVIOUS\", \"NETFLIX_MOVIE\", \"NETFLIX_TV\", \"BEDROOM_LIGHTS_ON\", \"BEDROOM_LIGHTS_OFF\", \"WEATHER_WIDGET\"]\nReturn a tuple in this format: \n(action, [optional_arguments,...]) \n in python code." % command,
        temperature=0,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    result = response["choices"][0]["text"]

    try:
        transcription = ast.literal_eval(result)
        return transcription
    except:
        return "There was an error transcribing to code."
