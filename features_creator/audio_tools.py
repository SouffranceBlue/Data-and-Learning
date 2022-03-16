import librosa 
import sounddevice as sd
import wavio


def read_audio(file):
    with open(file, "rb") as audio_file:
        audio_bytes = audio_file.read()
    return audio_bytes


def record(duration=10, fs=44000):
    sd.default.samplerate = fs
    sd.default.channels = 1
    sd.default.device = 0
    myrecording = sd.rec(int(duration * fs))
    sd.wait(duration)
    return myrecording


def save_record(path_myrecording, myrecording, fs):
    wavio.write(path_myrecording, myrecording, fs, sampwidth=2)
    return None