import tkinter
from tkinter import *

window=Tk()

window.title("Calculator")

# getting input values
def click(number) :
    temp= e.get()
    e.delete(0,END)
    e.insert (0,str(temp)+str(number))

# clear function
def clear() :
    e.delete(0,END)
    
# add
def add() :
    global operation
    operation = 'add'
    num =e.get()
    global mem
    mem = int(num)
    e.delete(0,END)

# subtraction
def sub() :
    global operation
    operation = 'sub'
    num =e.get()
    global mem
    mem = int(num)
    e.delete(0,END)

# divide
def div() :
    global operation
    operation = 'div'
    num =e.get()
    global mem
    mem = int(num)
    e.delete(0,END)

# multiplication
def mul() :
    global operation
    operation = 'mul'
    num =e.get()
    global mem
    mem = int(num)
    e.delete(0,END)


#result
def equal () :
    next_value = e.get()
    e.delete(0,END)

    if operation == "add" :
        e.insert(0,mem + int(next_value))
    if operation == "sub" :
        e.insert(0,mem - int(next_value))
    if operation == "mul" :
        e.insert(0,mem * int(next_value))
    if operation == "div" :
        e.insert(0,mem / int(next_value))

# buttons
button0= Button(window,text="0", padx=40,pady=20,command =lambda:click(0))
button1= Button(window,text="1", padx=40,pady=20,command =lambda:click(1))
button2= Button(window,text="2" ,padx=40,pady=20,command =lambda:click(2))
button3= Button(window,text="3" ,padx=40,pady=20,command =lambda:click(3))
button4= Button(window,text="4" ,padx=40,pady=20,command =lambda:click(4))
button5= Button(window,text="5" ,padx=40,pady=20,command =lambda:click(5))
button6= Button(window,text="6" ,padx=40,pady=20,command =lambda:click(6))
button7= Button(window,text="7" ,padx=40,pady=20,command =lambda:click(7))
button8= Button(window,text="8" ,padx=40,pady=20,command =lambda:click(8))
button9= Button(window,text="9" ,padx=40,pady=20,command =lambda:click(9))

button_add= Button(window,text="+" ,padx=40,pady=20,command =add)
button_mul= Button(window,text="*" ,padx=40,pady=20,command =mul)
button_sub= Button(window,text="-" ,padx=40,pady=20,command =sub)
button_div= Button(window,text="/" ,padx=40,pady=20,command =div)

button_equals= Button(window,text="=" ,padx=40,pady=20,command =equal)
button_clear= Button(window,text="C" ,padx=40,pady=20,command =clear)

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
