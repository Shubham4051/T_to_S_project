import pyttsx3
import uuid

engine = pyttsx3.init()
engine.setProperty("rate", 150)
text = input()


engine.say(text)
file_name = (str(uuid.uuid4())) + ".mp3"
engine.save_to_file(text, file_name)
engine.runAndWait()