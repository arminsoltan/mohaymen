from vosk import Model, KaldiRecognizer, SetLogLevel
import os
import wave


def speech_to_text(audio_file):
    wf = wave.open(audio_file, "rb")
    model = Model("vosk-model-fa-0.5")
    rec = KaldiRecognizer(model, wf.getframerate())
    flag = False
    text = None
    while not flag:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            text = rec.Result()
            return text
        else:
            text = rec.PartialResult()
        print(text)
    return text


if __name__ == "__main__":
    r = speech_to_text("test.wav")
