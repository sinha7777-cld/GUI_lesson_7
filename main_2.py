from tkinter import *
import random


root = Tk()
root.title("Color Magic")
root.geometry("300x300")

colors = ["red","blue","green","yellow","orange","purple"]

def change_color():
    random_color= random.choice(colors)
    root.config(bg=random_color)
    label.config(text="Change color:"+str( random_color))
    

label = Label(root,text="Color is:")
label.pack(pady=20)

btn = Button(text="Change color",command= change_color)
btn.pack(pady=20)

root.mainloop()