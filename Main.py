from googletrans import Translator
import os
import speech_recognition as sr

from SpeechToText import SpeechToText

def main():
    while True:
        print("Menu:")
        print("Type '1' to choose an audiofile.")
        print("Type '2' to start microphone and voice recorder.")
        print("Type '3' to Exit.")

        choice = input("Choose an option: ")

        if choice == "1":
            audiofile_path = input("Type the audiofile_path: ")
            if os.path.isfile(audiofile_path):
                # Do the audio file processing here
                print(f"You chose to insert the file: {audiofile_path}")

                # Translation here.
                stt = SpeechToText()
                with sr.AudioFile(audiofile_path) as source:
                    audio = stt.recognizer.record(source)
                text = stt.convert_speech_to_text(audio=audio)
                translate_and_print(text)
            else:
                print("File Not Found!")
        elif choice == "2":
            stt = SpeechToText()
            audio = stt.convert_speech_to_text()
            # Do the processing of the recorded audio here
            print("Audio recorded successfully!")

            # Translation here.
            text = stt.convert_speech_to_text(audio=audio)
            translate_and_print(text)
        elif choice == "3":
            print("Ending Program.")
            break
        else:
            print("Invalid option! Try again.")

def translate_and_print(text):
    translator = Translator()
    translation = translator.translate(text)
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

if __name__ == "__main__":
    main()