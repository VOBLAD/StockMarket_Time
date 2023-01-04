from tkinter import *
import pytz
from datetime import datetime
#------------------------------
def timeus():
    home = pytz.timezone("America/New_York")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clockus.config(text=current_time)
    clockus.after(200, timeus)
#------------------------------
def timeeu():
    home = pytz.timezone("Europe/London")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clockeu.config(text=current_time)
    clockeu.after(200, timeeu)
#------------------------------
def timech():
    home = pytz.timezone("Asia/Hong_Kong")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clockch.config(text=current_time)
    clockch.after(200, timech)
#------------------------------
def timeru():
    home = pytz.timezone("Europe/Moscow")
    local_time = datetime.now(home)
    current_time = local_time.strftime("%a %H:%M:%S")
    clockru.config(text=current_time)
    clockru.after(200, timeru)
#------------------------------
root = Tk()
root.resizable(False, False)
root.geometry("670x300")
root.title("StockTime")
root.config(bg="black")
#------------------------------
img = PhotoImage(file="1.png")
lbl = Label(root, image=img)
lbl.pack()
#------------------------------
clockus = Label(root, bg="black", fg="white", font="arial 15 bold")
clockus.place(x=28, y=140)
#------------------------------
clockeu = Label(root, bg="black", fg="white", font="arial 15 bold")
clockeu.place(x=190, y=140)
#------------------------------
clockch = Label(root, bg="black", fg="white", font="arial 15 bold")
clockch.place(x=350, y=140)
#------------------------------
clockru = Label(root, bg="black", fg="white", font="arial 15 bold")
clockru.place(x=510, y=140)
#------------------------------
imageus = PhotoImage(file="united-states.png")
usa_icon = Label(root, image=imageus, bg="black")
usa_icon.place(x=60, y=50)
#------------------------------
imageeu = PhotoImage(file="european-union.png")
eu_icon = Label(root, image=imageeu, bg="black")
eu_icon.place(x=220, y=50)
#------------------------------
imagechina = PhotoImage(file="china.png")
china_icon = Label(root, image=imagechina, bg="black")
china_icon.place(x=380, y=50)
#------------------------------
imagerussia = PhotoImage(file="russia.png")
russia_icon = Label(root, image=imagerussia, bg="black")
russia_icon.place(x=540, y=50)
#------------------------------
stockus = Label(root, text="Открытие:17:30(мск)\nЗакрытие:00:00(мск)", bg="black", fg="white", font="arial 10 bold")
stockus.place(x=27, y=180)
#------------------------------
stockeu = Label(root, text="Открытие:11:00(мск)\nЗакрытие:19:30(мск)", bg="black", fg="white", font="arial 10 bold")
stockeu.place(x=187, y=180)
#------------------------------
stockch = Label(root, text="Открытие:05:00(мск)\nЗакрытие:11:00(мск)", bg="black", fg="white", font="arial 10 bold")
stockch.place(x=347, y=180)
#------------------------------
stockru= Label(root, text="Открытие:10:00(мск)\nЗакрытие:23:50(мск)", bg="black", fg="white", font="arial 10 bold")
stockru.place(x=507, y=180)
#------------------------------
timeru()
timech()
timeeu()
timeus()
root.mainloop()