
from tkinter import *


import random


import base64


root = Tk()


root.geometry("1200x600")


root.title(" Encryption and Decryption")

Tops = Frame(root, width=150, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=100, relief=SUNKEN)
f1.pack(side=TOP)




lblInfo = Label(Tops, font=('times new roman', 25, 'bold'),
                text="Encryption and Decryption",
                fg="Black", bd=100, anchor='w')

lblInfo.grid(row=0, column=0)



Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()



lblMsg = Label(f1, font=('times new roman', 16, 'bold'),
               text="MESSAGE", bd=5, anchor="w")

lblMsg.grid(row=1, column=0)

txtMsg = Entry(f1, font=('times new roman', 16, 'bold'),
               textvariable=Msg, bd=10, insertwidth=4,
               bg="powder blue", justify='left')


txtMsg.grid(row=1, column=1)

lblkey = Label(f1, font=('times new roman', 16, 'bold'),
               text="KEY (Only Integer)", bd=16, anchor="w")

lblkey.grid(row=2, column=0)



txtkey = Entry(f1, font=('times new roman', 16, 'bold'),
               textvariable=key, bd=10, insertwidth=4,
               bg="powder blue", justify='left')

txtkey.grid(row=2, column=1)


lblmode = Label(f1, font=('times new roman', 16, 'bold'),
                text="Encryption or Decryption ",
                bd=16, anchor="w")

lblmode.grid(row=3, column=0)

txtmode = Entry(f1, font=('times new roman', 16, 'bold'),
                textvariable=mode, bd=10, insertwidth=4,
                bg="powder blue", justify='left')

txtmode.grid(row=3, column=1)


lblResult = Label(f1, font=('times new roman', 16, 'bold'),
                  text="The Result : ", bd=16, anchor="w")

lblResult.grid(row=2, column=2)


txtResult = Entry(f1, font=('times new roman', 16, 'bold'),
                  textvariable=Result, bd=10, insertwidth=4,
                  bg="powder blue", justify='left')

txtResult.grid(row=2, column=3)



def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(msg[i]) +
                     ord(key_c)) % 256)
        enc.append(enc_c)
        print("enc:", enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()




def decode(key, enc):
    dec = []

    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) -
                     ord(key_c)) % 256)

        dec.append(dec_c)
        print("dec:", dec)
    return "".join(dec)


def Results():
  

    msg = Msg.get()
    k = key.get()
    m = mode.get()

    if (m == 'encryption'):
        Result.set(encode(k, msg))
    else:
        Result.set(decode(k, msg))




def qExit():
    root.destroy()



def Reset():

    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")



btnTotal = Button(f1, padx=16, pady=8, bd=16, fg="black",bg="powder blue",
                  font=('times new roman', 16, 'bold'), width=10,
                  text="Show Message", 
                  command=Results).grid(row=7, column=1)


btnReset = Button(f1, padx=16, pady=8, bd=16,bg="powder blue",
                  fg="black", font=('times new roman', 16, 'bold'),
                  width=10, text="Reset", 
                  command=Reset).grid(row=7, column=2)


btnExit = Button(f1, padx=16, pady=8, bd=16,bg="powder blue",
                 fg="black", font=('times new roman', 16, 'bold'),
                 width=10, text="Exit", 
                 command=qExit).grid(row=7, column=3)


root.mainloop()