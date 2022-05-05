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

def BindPlus(event):
    global LaatstUp
    global LaatstDown
    LaatstUp = 1
    LaatstDown = 0
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
    

window.bind("=", BindPlus)

def BindMin(event):
    global Score
    global LaatstUp
    global LaatstDown
    Score -= 1
    LaatstUp = 0
    LaatstDown = 1
    print(Score)
    label['text'] = Score
    if Score > 0:
        window.config(bg='green')
    if Score == 0:
        window.config(bg='grey')
    if Score < 0:
        window.config(bg='red')

    
window.bind("-", BindMin)

LaatstUp = 0
def ChangeLaatstUp(event):
    global LaatstUp
    global LaatstDown
    LaatstUp = 1
    LaatstDown = 0
    print(f"up {LaatstUp}")
    print(f"down {LaatstDown}")

LaatstDown = 0
def ChangeLaatstDown(event):
    global LaatstUp
    global LaatstDown
    LaatstUp = 0
    LaatstDown = 1
    print(f"up {LaatstUp}")
    print(f"down {LaatstDown}")
    
buttonUp = tk.Button(window, text="Up", command=Plus)
buttonUp.pack(ipadx=10,ipady=10, fill='x', expand=True)
buttonUp.bind("<Button>", ChangeLaatstUp)


label = tk.Label(window, text= 0)
label.pack(ipadx=10,ipady=10, fill='x', expand=True)

def MultiplyAndDivide(event):
    global Score
    if LaatstUp == 1:
        Score *= 3
        label['text'] = Score
    elif LaatstDown == 1:
        Score /= 3
        label['text'] = Score

label.bind("<Double-Button>", MultiplyAndDivide)
window.bind("<space>", MultiplyAndDivide)

def ClearScore(event):
    global Score
    Score = 0
    label['text'] = Score

label.bind("<Triple-Button-3>", ClearScore)

buttonDown = tk.Button(window, text="Down", command=Min)
buttonDown.pack(ipadx=10,ipady=10, fill='x', expand=True)
buttonDown.bind("<Button>", ChangeLaatstDown)

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

window.mainloop()