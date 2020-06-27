

# calculator

from tkinter import *
import tkinter.ttk as ttk


window=Tk()

'''
style = ttk.Style(window)
#style.theme_use("clam")
style.theme_use("classic")

style.map("C.TButton",
   foreground=[('!active', 'black'),('pressed', 'red'), ('active', 'white')],
    background=[ ('pressed', 'white'), ('active', '#ffcce6')]
    )
'''

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
button0= ttk.Button(window,text="0",command =lambda:click(0))
button1= ttk.Button(window,text="1",command =lambda:click(1))
button2= ttk.Button(window,text="2" ,command =lambda:click(2))
button3= ttk.Button(window,text="3" ,command =lambda:click(3))
button4= ttk.Button(window,text="4" ,command =lambda:click(4))
button5= ttk.Button(window,text="5" ,command =lambda:click(5))
button6= ttk.Button(window,text="6" ,command =lambda:click(6))
button7= ttk.Button(window,text="7" ,command =lambda:click(7))
button8= ttk.Button(window,text="8" ,command =lambda:click(8))
button9= ttk.Button(window,text="9" ,command =lambda:click(9))

button_add= ttk.Button(window,text="+" ,command =add)
button_mul= ttk.Button(window,text="*" ,command =mul)
button_sub= ttk.Button(window,text="-" ,command =sub)
button_div= ttk.Button(window,text="/" ,command =div)

button_equals= ttk.Button(window,text="=", command =equal)
button_clear= ttk.Button(window,text="C" ,command =clear)

button0.grid(row=4,column=0,padx=0,pady=0)
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
button_div.grid(row=6,column=0)
button_equals.grid(row=6,column=1 ,columnspan =2,padx=0)
button_clear.grid(row=5,column=1,columnspan=2)


# output

e = Entry (window,width = 36 ,borderwidth =5)
e.grid(row=0,column =0,columnspan =3,padx=10,pady=20)




window.mainloop

