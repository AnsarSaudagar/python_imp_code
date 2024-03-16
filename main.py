import random
from tkinter import *
import pandas
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

print(to_learn)




def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    french_title = canvas.itemconfig(card_title, text="French", fill="black")
    french_text = canvas.itemconfig(card_text, text=current_card["French"], fill="black")
    canvas.itemconfig(front_canvas, image=front_image)
    flip_timer = window.after(3000, flip_card)


def flip_card():

    canvas.itemconfig(card_title, text="English", fill="white" )
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    back_card = canvas.itemconfig(front_canvas, image=back_image)

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
front_canvas = canvas.create_image(400, 263, image=front_image)

back_image = PhotoImage(file="images/card_back.png")

card_title = canvas.create_text(400, 150, text="", fill="black", font=("Arial", 40, "italic"))
card_text = canvas.create_text(400, 263, text="", fill="black", font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()



