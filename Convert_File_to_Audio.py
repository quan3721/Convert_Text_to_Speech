from gtts import gTTS
import os

# -- Open file -- #
text = open('demo.txt', 'r').read()

language = 'en'
output = gTTS(text=text, lang=language, slow=False) # -- convert
output.save('fileoutput.mp3') # -- save audio into a file audio

os.system('start fileoutput.mp3') # -- open file audio saved