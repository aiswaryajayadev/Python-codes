from tkinter import *
import datetime
import time
import winsound

clock = Tk()

def alam(set_alam_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alam_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break
def actual_time():
    set_alam_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alam(set_alam_timer)
    clock = Tk()
clock.title("Alarm clock")
clock.geometry("1000x500")
time_format=Label(clock, text = "Enter time in 24 hour format!", fg="black", bg="white",font="timesnewroman").place(x=60, y=120)
addTime = Label(clock, text="Hour   Min    Sec",font=60).place(x=110)
setYourAlam=Label(clock,text="Set Alarm : ",fg="blue",relief="solid", font=("times new roman",10,"bold")).place(x=0,y=29)
hour=StringVar()
min=StringVar()
sec=StringVar()
hourTime=Entry(clock,textvariable=hour, width=15).place(x=110,y=30)
minTime=Entry(clock,textvariable=min,width=15).place(x=150,y=30)
secTime=Entry(clock,textvariable=sec,width=15).place(x=200,y=30)
submit = Button(clock,text="Confirm ",fg="red",font=("times new roman",10,"bold"),width=10,command=actual_time).place(x=110,y=70)
clock.mainloop()