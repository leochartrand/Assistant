import sounddevice as sd
from scipy.io.wavfile import write

def listen():
    fs=44100
    duration=3
    print("...")
    audio=sd.rec(int(duration * fs),samplerate=fs,channels=2)
    sd.wait()       
    write("audio.wav",fs,audio)
