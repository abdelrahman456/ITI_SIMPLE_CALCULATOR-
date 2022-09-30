from tkinter import *
import tkinter as tk
from tkinter import messagebox
#import tkinter as tk
root = tk.Tk()

'''window_.title("hello world")
window_.geometry('500x500')
label_1= Label(window_, text ="Label1")

b1 = Button(window_, text= "Abdo")

#b2 = Button(window_, text= "raafat")
b3 = Button(window_, text= "mahrous")
b4 = Button(window_, text= "mahrous")
b1.pack(side= TOP)
#b2.pack(side= BOTTOM)
b3.pack(side= RIGHT)
b4.pack(side= LEFT)

label_1.pack(side= BOTTOM)



photo_1 = PhotoImage(file= 'cc.PNG')
photo_1=photo_1.subsample(2,2)
b_1= Button(window_, text= "close the window", bd = '5', image= photo_1)
b_1.pack(side= TOP)
'''
expression = ""
root.title("BANK SYSTEM")
root.geometry('300x100')
root.configure(background="light green")
name_var=tk.StringVar()
passw_var=tk.StringVar()
equation = tk.StringVar()
def calc():
    name =name_var.get()
    password= passw_var.get()
    if name=="abdo" and password=="1234":
        #root.destroy()
        New_Window()
def clear():
    global expression
    expression = "0"
    equation.set("0")
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.
 
    # Put that code inside the try block
    # which may generate the error
    try:
 
        global expression
 
        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))
 
        equation.set(total)
 
        # initialize the expression variable
        # by empty string
        expression = ""
 
    # if error is generate then handle
    # by the except block
    except:
 
        equation.set(" error ")
        expression = ""

def New_Window():
    #root.destroy()   
   
    Window = tk.Toplevel(root)
    #Window = Tk()
    
    Window.grid()
    
    Window.title("calculator")
    Window.geometry("312x324")  # this is for the size of the window 
    Window.resizable(0, 0)
   # Window.geometry('300x200')
    input_frame = tk.Frame(Window, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
    input_frame.pack(side=TOP)
 
    #Let us create a input field inside the 'Frame'
 
    input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=equation, width=50, bg="white", bd=0, justify=RIGHT)
    input_field.grid(row=0, column=0)
 
    input_field.pack(ipady=10)
    #expression_field = tk.Entry(Window, textvariable=equation, font = ('calibre',10,'bold'))
    btns_frame = tk.Frame(Window, width=312, height=272.5, bg="grey")
 
    btns_frame.pack()
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    #expression_field.grid(columnspan=4, ipadx=70)
    #num_label=tk.Label(Window,text='WINDOW', font = ('calibre',14,'bold'))
    zero=tk.Button(btns_frame, text=' 0 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("0"), height=3, width=21)
    zero.grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
    one=tk.Button(btns_frame, text=' 1 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("1"), height=3, width=10)
    one.grid(row = 3, column = 0, padx = 1, pady = 1)
    two=tk.Button(btns_frame, text=' 2 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("2"), height=3, width=10)
    two.grid(row = 3, column = 1, padx = 1, pady = 1)
    three=tk.Button(btns_frame, text=' 3 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("3"), height=3, width=10)
    three.grid(row = 3, column = 2, padx = 1, pady = 1)
    four=tk.Button(btns_frame, text=' 4 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("4"), height=3, width=10)
    four.grid(row = 2, column = 0, padx = 1, pady = 1)
    five=tk.Button(btns_frame, text=' 5 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("5"), height=3, width=10)
    five.grid(row = 2, column = 1, padx = 1, pady = 1)
    six=tk.Button(btns_frame, text=' 6 ', fg='black', bd = 0, bg = "#fff", command=lambda: press("6"), height=3, width=10)
    six.grid(row = 2, column = 2, padx = 1, pady = 1)               
    seven=tk.Button(btns_frame, text=' 7 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("7"), height=3, width=10)
    seven.grid(row = 1, column = 0, padx = 1, pady = 1)
    eight=tk.Button(btns_frame, text=' 8 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("8"), height=3, width=10)
    eight.grid(row = 1, column = 1, padx = 1, pady = 1)
    nine=tk.Button(btns_frame, text=' 9 ', fg='black', bd = 0, bg = "#fff",command=lambda: press("9"), height=3, width=10)
    nine.grid(row = 1, column = 2, padx = 1, pady = 1)
    plus=tk.Button(btns_frame, text=' + ', fg='black', bd = 0, bg = "#eee",command=lambda: press("+"), height=3, width=10)
    plus.grid(row = 3, column = 3, padx = 1, pady = 1) 
    minus=tk.Button(btns_frame, text=' - ', fg='black', bd = 0, bg = "#eee",command=lambda: press("-"), height=3, width=10)
    minus.grid(row = 2, column = 3, padx = 1, pady = 1)
    mul=tk.Button(btns_frame, text=' * ', fg='black', bd = 0, bg = "#eee",command=lambda: press("*"), height=3, width=10)
    mul.grid(row = 1, column = 3, padx = 1, pady = 1)
    div=tk.Button(btns_frame, text=' / ', fg='black', bd = 0, bg = "#eee",command=lambda: press("/"), height=3, width=10)
    div.grid(row = 0, column = 3, padx = 1, pady = 1)
    equal =tk.Button(btns_frame, text=' = ', fg='black', bd = 0, bg = "#eee",command=equalpress, height=3, width=10)
    equal.grid(row = 4, column = 3, padx = 1, pady = 1)
    #equal.pack()
    clear =tk.Button(btns_frame, text='C', fg='black', bd = 0, bg = "#eee",command=equalpress, height=3, width=32)
    clear.grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
    #name_label.grid(row=0,column=0)
    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: press(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
    #canvas = tk.Canvas(Window, height=10, width=20)
    
    #canvas.pack()
    #Window.mainloop()
def press(num):
    # point out the global expression variable
    global expression
 
    # concatenation of string
    expression = expression + str(num)
 
    # update the expression by using set method
    equation.set(expression)
def submit():
        name =name_var.get()
        password= passw_var.get()
        print("the name is :"+name)
        print("the password is :", password)
        name_var.set("")
        passw_var.set("")
        

name_label=tk.Label(root,text='username', font = ('calibre',10,'bold'))
name_entry= tk.Entry(root, textvariable = name_var, font = ('calibre',10,'bold')) 
password_label= tk.Label(root,text='password', font = ('calibre',10,'bold'))     
password_entry= tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'bold'), show ='*')    

#button=tk.Button(root, text ='submit', command = submit)
sub_btn = tk.Button(root, text="calculator", bg='White', fg='Black',
                              command = lambda:  calc())

#button.grid(row=5,column=5)
name_label.grid(row=0,column=0)
password_label.grid(row=1,column=0)
name_entry.grid(row=0,column=1)
password_entry.grid(row=1,column=1)
sub_btn.grid(row=2,column=1)
root.mainloop()