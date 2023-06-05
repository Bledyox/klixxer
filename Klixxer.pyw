"""
Titel:    Klixxer
Version:  1.0
Autor:    Sascha M. Schumacher
"""

# Imports
from tkinter import *
from random import randint

# Functions
def start():
    # Pop-Up Window create
    global winPop
    winPop = Tk()
    winPop.title("")
    winPop.iconbitmap(default='Klixxer.ico')
    # Pop-Up Window size and position
    w = 150
    h = 30
    x = randint(0, winPop.winfo_screenwidth() - 75)
    y = randint(0, winPop.winfo_screenheight() - 75)
    winPop.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Pop-Up Window
    btnClick = Button(winPop, text = "Klick mich!", width = 15, command = click, font = ("Arial", 20))
    btnClick.pack()
    # Pop-Up Window end
    winPop.mainloop()

def click():
    # Pop-Up Window create
    global winPop
    winPop.destroy()
    winPop = Tk()
    winPop.title("")
    winPop.iconbitmap(default='Klixxer.ico')
    # Pop-Up Window size and position
    w = 150
    h = 30
    x = randint(0, winPop.winfo_screenwidth() - 75)
    y = randint(0, winPop.winfo_screenheight() - 75)
    winPop.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Pop-Up Window
    btnClick = Button(winPop, text = "Klick mich!", width = 15, command = click, font = ("Arial", 20))
    btnClick.pack()
    # Pop-Up Window end
    winPop.mainloop()

def kill():
    global winRoot
    winRoot.destroy()
    global winPop
    winPop.destroy()
    global winInfo
    winInfo.destroy()

def info():
    # Info Window create
    global winInfo
    winInfo = Tk()
    winInfo.title("Klixxer - Info")
    winInfo.iconbitmap(default='Klixxer.ico')
    # Info Window size and position
    w = 250
    h = 80
    x = ((winInfo.winfo_screenwidth()/2)  - (w/2))
    y = ((winInfo.winfo_screenheight()/2) - (h/2))
    winInfo.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # Info Window
    lblTitle = Label(winInfo, text = "Titel:        Klixxer", font = ("Arial", 10))
    lblTitle.place(x = 10, y = 10)
    lblVersion = Label(winInfo, text = "Version:   1.0", font = ("Arial", 10))
    lblVersion.place(x = 10, y = 30)
    lblAuthor = Label(winInfo, text = "Autor:      Sascha M. Schumacher", font = ("Arial", 10))
    lblAuthor.place(x = 10, y = 50)
    # Info Window end
    winInfo.mainloop()

# Root Window create
global winRoot
winRoot = Tk()
winRoot.title("Klixxer")
winRoot.iconbitmap(default='Klixxer.ico')
# Root Window size and position
w = 500
h = 100
x = ((winRoot.winfo_screenwidth()/2)  - (w/2))
y = ((winRoot.winfo_screenheight()/2) - (h/2))
winRoot.geometry('%dx%d+%d+%d' % (w, h, x, y))
# Root Window
lblTitle = Label(winRoot, text = "Klixxer", font = ("Arial", 20))
lblTitle.place(x = 210, y = 10)
btnStart = Button(winRoot, text = "Start", width = 10, command = start, font = ("Arial", 10))
btnStart.place(x = 50, y = 50)
btnKill = Button(winRoot, text = "Exit", width = 10, command = kill, font = ("Arial", 10))
btnKill.place(x = 210, y = 50)
btnInfo = Button(winRoot, text = "Info", width = 10, command = info, font = ("Arial", 10))
btnInfo.place(x = 370, y = 50)
# Root Window end
winRoot.mainloop()
