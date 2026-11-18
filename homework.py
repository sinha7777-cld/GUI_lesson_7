from tkinter import *
import random
import tkinter.font as font

root = Tk()
root.title("Coin Toss")
root.geometry("600x500")

options = ["Heads","Tails"]

def flip_coin():
    result = random.choice(options)

label_1 = Label(root,text="Coin Toss",font=font.Font(size=20),fg="Grey")
label_1.pack(pady=10)

label_2 = Label(root,text="Let's Start the Game....",fg="Green",font=font.Font(size=15))
label_2.pack(pady=10)

frame = Frame(root)
frame.pack()

label_3 = Label(frame,text="Coin Toss:",fg="grey",font=font.Font(size=15))
label_3.grid(row=0,column=0,pady=10)

btn_1 = Button(frame,text="Flip Coin",bg="yellow")
btn_1.grid(row=1,column=1,padx=8,pady=5)

label_4 = Label(frame,text="Result:",fg="grey",font=font.Font(size=15))
label_4.grid(row=2,column=0,pady=10)

label_5 = Label(frame,text="Coin Result:-",font=font.Font(size=12))
label_5.grid(row=3,column=1,pady=10,padx=10)

root.mainloop()

