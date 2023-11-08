# -- Giao diện cho App convert text to Speech -- #

# -- Import Libraries -- #
from gtts import gTTS
import os
from tkinter import *

# -- Create a function to convert to speech -- #
def textToSpeech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')

# -- Create a window from tkinter library -- #
root = Tk()

# -- Create a canvas to set up width and height of the window -- #
canvas = Canvas(root, width=400, height=300)
canvas.pack()


# -- Create entry for entering input -- #
entry = Entry(root)
canvas.create_window(200, 180, window=entry) # -- 200 an 180 the position of entry ( 200 : width, 180 : height )

# -- Create button -- #
button = Button(text="Start", command=textToSpeech)
canvas.create_window(200, 230, window=button)

root.mainloop()