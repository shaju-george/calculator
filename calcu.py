# calculator

from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
from math import factorial as fac
from math import log10 as logof
from math import pow as power
from math import sqrt as square_root
from math import sin as sine
from math import cos as cose
from math import tan as tangent
import math
import datetime
import webbrowser
from time import sleep




window=Tk()


#s#h#a#j#u
window.title("Calculator")

window.geometry('452x440')
window.configure(bg='#f9ecec')
window.resizable(0,0)


#icon
window.iconbitmap('calculator1.ico')


#menu
def blue():
       window.configure(bg='#000099')     
def dark():
       window.configure(bg='black')
def white():
       window.configure(bg='white')
def default():
       window.configure(bg='#f9ecec')  

def time():
    now = datetime.datetime.now()
    e.delete(0,END)
    e.insert(0 ,now)
def title():
    name1 = input('Enter your name :')
    e.insert(0 ,"hi " +name1 +" !")
    name = input('Enter New title for calculator :')
    window.title(name)

    
def helppp():
    webbrowser.open('https://www.quora.com/', new=2)
def cross():
    webbrowser.open('https://www.youtube.com/channel/UCoGHeFY7jE2OB_TJS_87MOA', new=2)

my_menu = Menu(window)
window.config(menu = my_menu)

Menus = Menu(my_menu)
my_menu.add_cascade(label ='Menu',menu=Menus)
Menus.add_command (label ='Date & Time',command=time)
Menus.add_separator()
Menus.add_command (label ='Help',command=  helppp)
Menus.add_separator()
Menus.add_command (label ='Change Title',command= title)
Menus.add_separator()
Menus.add_command (label ='Exit',command=  quit)
Menus.add_separator()

views = Menu(my_menu)
my_menu.add_cascade(label ='Views',menu=views)
views.add_command (label ='White',command=white)
views.add_separator()
views.add_command (label ='Dark',command=dark)
views.add_separator()
views.add_command (label ='Blue',command=blue)
views.add_separator()
views.add_command (label ='Default',command=default)

team = Menu(my_menu)
my_menu.add_cascade(label ='About',menu=team)
team.add_command (label ='Team',command=cross)

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
    
    num =e.get()
    e.delete(0,END)
    e.insert(0 ,num + '+')
    
# subtraction
def sub() :
    
    num =e.get()
    e.delete(0,END)
    e.insert(0 ,num + '-')

# divide
def div() :
    
    num =e.get()
    e.delete(0,END)
    e.insert(0 ,num + '/')

# multiplication
def mul() :
    
    num =e.get()
    e.delete(0,END)
    e.insert(0 ,num + '*')

def equal():
    equation= e.get()
    e.delete(0,END)
    try :
        e.insert(0,eval(equation))
    except ZeroDivisionError:
        messagebox.showerror("Error","Division by zero not supported ")
    except ValueError :
        messagebox.showerror("Error","Value error , invalid input {eg : log(-x)}")
    global mem
    mem = eval(equation)
        
# Prev answer
def ans():
    temp= e.get()
    e.delete(0,END)
    
    e.insert(0, mem)

#dot button
def dot():
    temp= e.get()
    e.delete(0,END)
    e.insert (0,temp+".")
    
def back():
    c = e.get()
    e.delete(0,END)
    e.insert(0,c[:-1])

def fact():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'fac(' + num + ')' )

def log():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'logof(' +str(num)+')')


def sin():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'sine(' +str(num)+')')

def cos():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'cose(' +str(num)+')')

def tan():
   
    num =e.get()
    e.delete(0,END)
    e.insert(0,'tangent(' +str(num)+')')

def sqrt():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'square_root(' +str(num)+')')


def pow1():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,'power('+num +',')

def opening():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,num+'(')

def closing():
    
    num =e.get()
    e.delete(0,END)
    e.insert(0,num+')')
    
def pi():

    num =e.get()
    e.delete(0,END)
    e.insert(0,num + str(math.pi))

def math_e():

    num =e.get()
    e.delete(0,END)
    e.insert(0,num + str(math.e))

memory = 0
def m_plus():
    global memory
    memory1 = e.get()
    try :
        a= eval(memory1)
    except ZeroDivisionError:
        messagebox.showerror("Error","Division by zero not supported ")
    except ValueError :
        messagebox.showerror("Error","Value error , invalid input {eg : log(-x)}")
    memory = memory + a
    e.delete(0,END)
    
def m_minus():
    global memory
    memory1 = e.get()
    try :
        a= eval(memory1)
    except ZeroDivisionError:
        messagebox.showerror("Error","Division by zero not supported ")
    except ValueError :
        messagebox.showerror("Error","Value error , invalid input {eg : log(-x)}")
    memory = memory - a
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
button_mul= ttk.Button(window,text="x" ,command =mul)
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

button_opening = ttk.Button(window,text="(",command = opening)
button_closing = ttk.Button(window,text=")",command = closing)


#button0.shaju.place(height=80, width=100, x=300, y=300)
button_pi.grid(row=1,column=0,padx=2,pady=2,ipadx=5,ipady=10)
button_mr.grid(row=1,column=2,padx=2,pady=0,ipadx=5,ipady=10)
button_mc.grid(row=1,column=1,padx=2,pady=0,ipadx=5,ipady=10)
button_mp.grid(row=1,column=3,padx=2,pady=0,ipadx=5,ipady=10)
button_mm.grid(row=1,column=4,padx=2,pady=0,ipadx=5,ipady=10)

button_e.grid(row=2,column=0,padx=0,pady=2,ipadx=5,ipady=10)
button_log.grid(row=2,column=1,padx=0,pady=0,ipadx=5,ipady=10)
button_sin.grid(row=2,column=2,padx=0,pady=0,ipadx=5,ipady=10)
button_cos.grid(row=2,column=3,padx=0,pady=0,ipadx=5,ipady=10)
button_tan.grid(row=2,column=4,padx=0,pady=0,ipadx=5,ipady=10)

button_back.grid(row=3,column=3,padx=0,pady=2,ipadx=5,ipady=10)
button_fact.grid(row=3,column=0,padx=0,pady=0,ipadx=5,ipady=10)
button_sqrt.grid(row=3,column=1,padx=0,pady=0,ipadx=5,ipady=10)
button_div.grid(row=3,column=4,padx=0,pady=0,ipadx=5,ipady=10)
button_clear.grid(row=3,column=2,padx=0,pady=0,ipadx=5,ipady=10)

button_pow.grid(row=4,column=0,padx=0,pady=2,ipadx=5,ipady=10)
button7.grid(row=4,column=3,padx=0,pady=2,ipadx=5,ipady=10)
button8.grid(row=4,column=2,padx=0,pady=2,ipadx=5,ipady=10)
button9.grid(row=4,column=1,padx=0,pady=2,ipadx=5,ipady=10)
button_mul.grid(row=4,column=4,padx=0,pady=2,ipadx=5,ipady=10)

button4.grid(row=5,column=3,padx=0,pady=2,ipadx=5,ipady=10)
button5.grid(row=5,column=2,padx=0,pady=2,ipadx=5,ipady=10)
button6.grid(row=5,column=1,padx=0,pady=2,ipadx=5,ipady=10)
button_sub.grid(row=5,column=4,padx=0,pady=2,ipadx=5,ipady=10)
button_ans.grid(row=5,column=0,padx=0,pady=2,ipadx=5,ipady=10)

button_opening.grid(row=6,column=0,padx=0,pady=2,ipadx=5,ipady=10)
button1.grid(row=6,column=3,padx=0,pady=0,ipadx=5,ipady=10)
button2.grid(row=6,column=2,padx=0,pady=0,ipadx=5,ipady=10)
button3.grid(row=6,column=1,padx=0,pady=0,ipadx=5,ipady=10)
button_add.grid(row=6,column=4,padx=0,pady=0,ipadx=5,ipady=10)

button_dot.grid(row=7,column=1,padx=0,pady=2,ipadx=5,ipady=10)
button0.grid(row=7,column=2,padx=0,pady=2,ipadx=5,ipady=10)
button_closing.grid(row=7,column=0,padx=0,pady=2,ipadx=5,ipady=10)
button_equals.grid(row=7,column=3 ,columnspan =2,padx=0,pady=2,ipadx=48,ipady=10)


# output

e = Entry (window,width = 36 ,borderwidth =10)
e.grid(row=0,column =0,columnspan =5,ipadx=50,pady=5,ipady=12)



window.mainloop
