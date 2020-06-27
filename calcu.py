import tkinter
from tkinter import *

window=Tk()

window.title("Calculator")

def click() :
    pass

# buttons
button0= Button(window,text="0", padx=40,pady=20,command=click)
button1= Button(window,text="1", padx=40,pady=20,command =click)
button2= Button(window,text="2" ,padx=40,pady=20,command =click)
button3= Button(window,text="3" ,padx=40,pady=20,command =click)
button4= Button(window,text="4" ,padx=40,pady=20,command =click)
button5= Button(window,text="5" ,padx=40,pady=20,command =click)
button6= Button(window,text="6" ,padx=40,pady=20,command =click)
button7= Button(window,text="7" ,padx=40,pady=20,command =click)
button8= Button(window,text="8" ,padx=40,pady=20,command =click)
button9= Button(window,text="9" ,padx=40,pady=20,command =click)
button_add= Button(window,text="+" ,padx=40,pady=20,command =click)
button_mul= Button(window,text="*" ,padx=40,pady=20,command =click)
button_sub= Button(window,text="-" ,padx=40,pady=20,command =click)
button_div= Button(window,text="/" ,padx=40,pady=20,command =click)
button_equals= Button(window,text="=" ,padx=40,pady=20,command =click)
button_clear= Button(window,text="C" ,padx=40,pady=20,command =click)

button0.grid(row=4,column=0)
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button_add.grid(row=4,column=1)
button_mul.grid(row=5,column=0)
button_sub.grid(row=4,column=2)
button_div.grid(row=5,column=1)
button_equals.grid(row=6,column=0)
button_clear.grid(row=5,column=2)


# output

e = Entry (window,width = 36 ,borderwidth =5)
e.grid(row=0,column =0,columnspan =3,padx=10,pady=20)




window.mainloop
