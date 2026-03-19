from tkinter import * 
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 31/data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    ramdom_card = random.choice(to_learn)
    current_card = ramdom_card
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=ramdom_card["French"], fill="black")      



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 31/images/card_front.png")
canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 31/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="/Users/anamika/Documents/100_Days_of_Python/100-Days-Of-Python/Day 31/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

next_card()

window.mainloop()

