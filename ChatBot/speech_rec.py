import speech_recognition as sr


def speak_func(lang, chat):
    r = sr.Recognizer()
    with sr.Microphone(device_index=12) as source:
        r.adjust_for_ambient_noise(source)
        print('Speak Anything: ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language=lang)
            return text
        except Exception:
            return 'Sorry, we could not recognize your voice'
