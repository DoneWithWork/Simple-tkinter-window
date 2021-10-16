# Importing tkinter packages
from tkinter import *

# Creating window and name it win
win = Tk()

# Window title
win.title("Tkinter Window")

# Window size
win.geometry("500x500")

# Don't allow window to resize
# 0 means no resize
win.resizable(0, 0)

# Simple text
text1 = Label(win, text="Hello World",
              fg="red")  # Draw text to win(screen) with the text Hello world and have a colour of red

# Setting data for text
text1.config(font=("Courier", 40, "bold"),
             bg="cyan")  # setting font, font size and making it bold with a background of cyan

# Putting text on screen
text1.pack()

# Setting background colour of window
win.configure(bg="yellow")

# Keeping window open
win.mainloop()
