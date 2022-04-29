from distutils.command.config import config
import tkinter as tk
from turtle import window_width

Score = 0

def Plus():
    global Score
    Score += 1
    print(Score)
    label['text'] = Score
    if Score > 0:
        window.config(bg='green')
    if Score == 0:
        window.config(bg='grey')
    if Score < 0:
        window.config(bg='red')
    

def Min():
    global Score
    Score -= 1
    print(Score)
    label['text'] = Score
    if Score > 0:
        window.config(bg='green')
    if Score == 0:
        window.config(bg='grey')
    if Score < 0:
        window.config(bg='red')

window = tk.Tk()
window.title("test")
window.geometry('500x200')
window.config(bg='pink')

buttonUp = tk.Button(window, text="Up", command=Plus)
buttonUp.pack(ipadx=10,ipady=10, fill='x', expand=True)

label = tk.Label(window, text= 0)
label.pack(ipadx=10,ipady=10, fill='x', expand=True)

def ChangeEnter(event):
    window.config(bg="yellow")

label.bind("<Enter>", ChangeEnter)

def ChangeLeave(event):
    if Score > 0:
        window.config(bg='green')
    if Score == 0:
        window.config(bg='grey')
    if Score < 0:
        window.config(bg='red')

label.bind("<Leave>", ChangeLeave)    

buttonDown = tk.Button(window, text="Down", command=Min)
buttonDown.pack(ipadx=10,ipady=10, fill='x', expand=True)


window.mainloop()