import pipeline
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ""
        try:
            result = r.recognize_google(audio, show_all=True)
            text = result["alternative"][0]["transcript"]
        except Exception as e:
            # print("Exception: " + str(e))
            pass
    return text.lower()

wake_word = "assistant"

print("Listening")

while True:
    text = get_audio()
    if text.count(wake_word) > 0:
        success = pipeline.main()
