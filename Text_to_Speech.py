from gtts import gTTS
import os

my_text = "Welcome to CodeChick Github"

speech = gTTS(text=my_text, lang='en', slow=False)

speech.save("welcome.mp3")