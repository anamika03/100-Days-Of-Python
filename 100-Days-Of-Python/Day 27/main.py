# GUI Graphical User Interface
import tkinter

window = tkinter.Tk()   # Create a window
window.title("My First GUI Program")  # Set the title of the window
window.minsize(width=500, height=300) # Set minimum size of the window

my_lebel = tkinter.Label(text="I am a Label", font=("Arial", 14)) # Create a label
my_lebel.pack()  # Place the label on the window

my_lebel["text"] = "New Text"  # Update the text of the label
my_lebel.config(text="Another New Text")  # Another way to update the text of

# Button
def button_clicked():
    print("I got clicked")
    input_text = input.get()  # Get text from input field
    my_lebel.config(text=input_text)

button = tkinter.Button(text="Click Me", command=button_clicked)  # Create a button and attach a function to it
button.pack()

# Input Field
input = tkinter.Entry(width=30)
input.pack()


# Keep the window open
window.mainloop() 
