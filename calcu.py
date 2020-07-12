# calculator

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import math

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
#s#h#a#j#u
window.title("Calculator")

window.geometry('425x600')
window.configure(bg='#f9ecec')
window.resizable(0,0)

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
#   operation = 'add'
    num =e.get()
   # global mem
   # mem = float(num)
    e.delete(0,END)
    e.insert(0 ,num + '+')
    

# subtraction
def sub() :
    global operation
    operation = 'sub'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)

# divide
def div() :
    global operation
    operation = 'div'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)

# multiplication
def mul() :
    global operation
    operation = 'mul'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
'''
def equal():
    value = e.get()
    e.delete(0,END)
    global t
    if operation == "add" :
        e.insert(0,float(value))
        
        t = float(value)

#result
def equal () :
    next_value = e.get()
    e.delete(0,END)
    global t
    if operation == "add" :
        e.insert(0,mem + float(next_value))
        
        t = mem + float(next_value)
    if operation == "sub" :
        e.insert(0,mem - float(next_value))
        t = mem - float(next_value)
    if operation == "mul" :
        e.insert(0,mem * float(next_value))
        t = mem * float(next_value)
    if operation == "div" :
        if float(next_value)== 0:
            messagebox.showerror("Error","Division by zero not supported")
        else:
            e.insert(0,mem / float(next_value))
            t = mem / float(next_value)
    if operation == "fact" :
        e.insert(0,math.factorial(mem))
        t = math.factorial(mem)
    if operation == "log" :
        e.insert(0,math.log10(mem))
        t = math.log10(mem)
    if operation == "sin" :
        e.insert(0,math.sin(mem))
        t = math.sin(mem)
    if operation == "tan" :
        e.insert(0,math.tan(mem))
        t = math.tan(mem)
    if operation == "cos" :
        e.insert(0,math.cos(mem))
        t = math.cos(mem)
    if operation == "sqrt" :
        e.insert(0,math.sqrt(mem))
        t = math.sqrt(mem)
    if operation == "pow" :
        e.insert(0,math.pow(mem,float(next_value)))
        t = math.pow(mem,float(next_value))
  '''
def equal():
    equation= e.get()
    e.delete(0,END)
    e.insert(0,eval(equation))
    global mem
    mem = eval(equation)
        
# Prev answer
def ans():
    e.delete(0,END)
    e.insert(0, mem)

#dot button
def dot():
    temp= e.get()
    e.delete(0,END)
    e.insert (0,str(temp)+".")
    
def back():
    c = e.get()
    e.delete(0,END)
    e.insert(0,c[:-1])

def fact():
    global operation
    operation = 'fact'
    num =e.get()
    global mem
    mem1 = float(num)
    mem = int(mem1)
    e.delete(0,END)
    e.insert(0,str(mem)+'!')

def log():
    global operation
    operation = 'log'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    e.insert(0,'log(' +str(num)+')')


def sin():
    global operation
    operation = 'sin'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    e.insert(0,'sin(' +str(num)+')')

def cos():
    global operation
    operation = 'cos'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    e.insert(0,'cos(' +str(num)+')')

def tan():
    global operation
    operation = 'tan'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    e.insert(0,'tan(' +str(num)+')')

def sqrt():
    global operation
    operation = 'sqrt'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    e.insert(0,'sqrt(' +str(num)+')')


def pow1():
    global operation
    operation = 'pow'
    num =e.get()
    global mem
    mem = float(num)
    e.delete(0,END)
    # e.insert(0,(str(num)+'^'))
    
def pi():
    global operation
    e.delete(0,END)
    e.insert(0,math.pi)

def math_e():
    global operation
    e.delete(0,END)
    e.insert(0,math.e)

memory = 0
def m_plus():
    global memory
    memory1 = e.get()
    memory = memory + float(memory1)
    e.delete(0,END)
    
def m_minus():
    global memory
    memory1 = e.get()
    memory = memory - float(memory1)
    e.delete(0,END)

def mr():
    global memory
    e.delete(0,END)
    if memory == 0:
        e.insert(0,'')
    else:
        e.insert(0,memory)
    
def mc():
    global memory
    memory = 0
    e.delete(0,END)


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

button_dot= ttk.Button(window,text="." ,command =dot)

button_equals= ttk.Button(window,text="=", command =equal)
button_clear= ttk.Button(window,text="C" ,command =clear)

button_back= ttk.Button(window,text="<-" ,command =back)
button_ans= ttk.Button(window,text="ans",command =ans)

button_fact= ttk.Button(window,text="x!",command =fact)
button_log= ttk.Button(window,text="log10",command =log)
button_sin= ttk.Button(window,text="sin",command =sin)
button_cos= ttk.Button(window,text="cos",command =cos)
button_tan= ttk.Button(window,text="tan",command =tan)
button_sqrt= ttk.Button(window,text="√",command =sqrt)
button_pow= ttk.Button(window,text="x^",command = pow1)
button_pi= ttk.Button(window,text="π",command = pi)
button_e= ttk.Button(window,text="e",command = math_e)

button_mr= ttk.Button(window,text="mr",command = mr)
button_mc= ttk.Button(window,text="mc",command = mc)
button_mp = ttk.Button(window,text="m+",command = m_plus)
button_mm = ttk.Button(window,text="m-",command = m_minus)
#button0.shaju.place(height=80, width=100, x=300, y=300)

button0.grid(row=4,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button1.grid(row=3,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button2.grid(row=3,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button3.grid(row=3,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button4.grid(row=2,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button5.grid(row=2,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button6.grid(row=2,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button7.grid(row=1,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button8.grid(row=1,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button9.grid(row=1,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_add.grid(row=1,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_mul.grid(row=3,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_sub.grid(row=2,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_div.grid(row=4,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_equals.grid(row=5,column=2 ,columnspan =2,padx=5,pady=5,ipadx=50,ipady=10)
button_clear.grid(row=4,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button_ans.grid(row=4,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_dot.grid(row=5,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_back.grid(row=5,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button_fact.grid(row=6,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button_sqrt.grid(row=6,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button_log.grid(row=6,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_sin.grid(row=6,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_cos.grid(row=7,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_tan.grid(row=7,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button_pow.grid(row=7,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button_pi.grid(row=7,column=3,padx=5,pady=5,ipadx=10,ipady=10)
button_e.grid(row=8,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_mr.grid(row=9,column=0,padx=5,pady=5,ipadx=10,ipady=10)
button_mc.grid(row=9,column=1,padx=5,pady=5,ipadx=10,ipady=10)
button_mp.grid(row=9,column=2,padx=5,pady=5,ipadx=10,ipady=10)
button_mm.grid(row=9,column=3,padx=5,pady=5,ipadx=10,ipady=10)
# output

e = Entry (window,width = 36 ,borderwidth =5)
e.grid(row=0,column =0,columnspan =4,ipadx=40,pady=10,ipady=10)



window.mainloop
