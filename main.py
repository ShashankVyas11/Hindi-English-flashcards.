from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#517BC8"
data = pandas.read_csv("data/hindi_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Hindi", fill="orange")
    canvas.itemconfig(card_word, text=current_card["Hindi"], fill="green")
    flip_timer = windows.after(7000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="orange")
    canvas.itemconfig(card_word, text=current_card["English"], fill="green")
    canvas.itemconfig(card_background, image=card_back_image)
    canvas.itemconfig(card_background, image=card_front_image)

def is_known():
    to_learn.remove(current_card)
    next_card()




windows = Tk()
windows.title("hindi-english")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = windows.after(4000, func=flip_card)

canvas = Canvas(width=800, height=550)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 225, image=card_front_image)
canvas.create_image(400, 225, image=card_front_image)
card_title = canvas.create_text(400, 50, text="title", font=("Futura", 40, "italic"))
card_word = canvas.create_text(400, 225, text="word", font=("Futura", 40, "italic"))
creater_name = canvas.create_text(400, 525, text="Made with ♥️by Shashank Vyas", font=("Futura", 25, "italic"), fill="white")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)
right_image = PhotoImage(file="images/right.png")
tick_button = Button(image=right_image, highlightthickness=0, command=is_known)
tick_button.grid(row=1, column=1)
canvas.grid(row=0, column=0)

next_card()

windows.mainloop()






