# GUI Graphical User Interface
import tkinter

window = tkinter.Tk()   # Create a window
window.title("My First GUI Program")  # Set the title of the window
window.minsize(width=500, height=300) # Set minimum size of the window

my_level = tkinter.Label(text="I am a Label", font=("Arial", 14)) # Create a label
my_level.pack()  # Place the label on the window


# Keep the window open
window.mainloop() 
