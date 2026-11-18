from tkinter import *
import tkinter.font as font
import random

root = Tk()

root.title("Roll Dice")
root.geometry("300x300")

def get_random_number():
    random_number = random.randint(1,6)
    label_2.config(text=random_number)

label_1 = Label(text="Roll the Dice!")
label_1.pack(pady=10)

label_2 = Label(text=0,font= font.Font(size=30))
label_2.pack(pady=20)

btn = Button(text="Roll",bg="light blue",command=get_random_number)
btn.pack(pady=30)

root.mainloop()