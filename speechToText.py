import whisper
import torch

device = "cuda" if torch.cuda.is_available() else "cpu"
model = whisper.load_model("base.en").to(device)

def transcribe():
    return model.transcribe("audio.wav", fp16=False)["text"]
    