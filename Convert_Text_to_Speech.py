# -- Import Library gtts -- #
from gtts import gTTS

import os

# -- Create a text for converting -- #
text = "LOL This is really funny"

# -- Create a variable to assign after converting -- #
output = gTTS(text=text, lang='en', slow=False)
output.save('audio_out.mp3') # -- save to the file audio

os.system('start audio_out.mp3') # -- Window -- for running file audio
# os.system('afplay audio_out.mp3') # -- Mac