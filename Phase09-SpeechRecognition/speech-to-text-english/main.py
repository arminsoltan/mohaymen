import speech_recognition as sr


def speech_to_text(file_name):
    r = sr.Recognizer()
    harvard = sr.AudioFile(file_name)
    with harvard as source:
        audio = r.record(source)
    text = r.recognize_google(audio)
    return text
