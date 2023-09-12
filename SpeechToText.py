import speech_recognition as sr

class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def convert_speech_to_text(self, audio=None):
        try:
            if audio is None:
                with sr.Microphone() as source:
                    print("Please say something...")
                    audio = self.recognizer.listen(source)
                
            text = self.recognizer.recognize_google(audio, language="pt-BR")
            return text
        except sr.UnknownValueError:
            return "It was not possible to understand the speech."
        except sr.RequestError as e:
            return f"Error in the request to the speech recognition service: {str(e)}"

    
    def convert_audiofile_to_text(self, audiofile_path=None):
        try:
            if audiofile_path:
                with sr.AudioFile(audiofile_path) as source:
                    audio = self.recognizer.record(source)

            else:
                raise ValueError("You should select an audio file or activate your microphone")

            text = self.recognizer.recognize_google(audio, language="pt-BR")  # Recognition using Google Web Speech API
            return text
       
        except sr.UnknownValueError:
            return "It was not possible to understand the speech."
        except sr.RequestError as e:
            return f"Error in the request to the speech recognition service: {str(e)}"

