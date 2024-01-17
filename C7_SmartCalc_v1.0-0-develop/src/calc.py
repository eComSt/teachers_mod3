import ctypes,os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class rpn(ctypes.Structure):
     _fields_ = [("type", ctypes.c_int),("num", ctypes.c_double)]

def initial_window():
    root.attributes('-alpha',0.95)
    root.geometry("290x250")
    root.attributes('-topmost', True)
    root.title("Calculator")

def c_calc():
    st=ctypes.c_char_p(calc_entry.get().encode())
    calc_entry.delete(0, END)
    calc_entry.insert(END,f(st,x_val).num)

def graph():
    x_val=int(x_entry.get())
    x_min=int(x_min_e.get())
    x_max=int(x_max_e.get())
    y_min=int(y_min_e.get())
    y_max=int(y_max_e.get())
    newWindow2 = Toplevel(newWindow)
    newWindow2.title("Graph")
    newWindow2.geometry("500x525")
    newWindow2.attributes('-topmost', 'true')
    newWindow2.attributes('-alpha',0.85)
    canv = Canvas(newWindow2, width = 500, height = 500, bg = "lightgrey")
    st=ctypes.c_char_p(calc_entry.get().encode())
    for i in range(100000):
            x = x_min + i*(x_max-x_min)/100000
            y = f(st,x).num
            if y<y_max and y>y_min:
                x=500*(x-x_min)/(x_max-x_min)
                y=500*(y_max-y)/(y_max-y_min)
                canv.create_oval(x, y, x + 1, y - 1, fill = 'black')
    canv.pack()
    Label(newWindow2,width=200,text=f"Func:{calc_entry.get()} X={x_val} Y={f(st,x_val).num}").pack()

def cred_b():
    global newWindow3
    def graph_cred():
        a=c(ctypes.c_double(int(s.get())),ctypes.c_int(int(t.get())),ctypes.c_double(float(p.get())),ctypes.c_char(e.get().encode()))
        os.system("open graph.txt")
    try:
        newWindow3.destroy()
    except:pass
    newWindow3 = Toplevel(root)
    newWindow3.title("Graph")
    newWindow3.geometry("200x120")
    newWindow3.attributes('-topmost', 'true')
    newWindow3.attributes('-alpha',0.9)
    Label(newWindow3,width=10,text="Сумма").grid(row=0,column=0,columnspan=1)
    s = Entry(newWindow3, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    s.insert(END,1000000)
    s.grid(row = 0, column = 1, columnspan = 1)
    Label(newWindow3,width=10,text="Срок").grid(row=1,column=0,columnspan=1)
    t = Entry(newWindow3, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    t.grid(row = 1, column = 1, columnspan = 1)
    t.insert(END,360)
    Label(newWindow3,width=10,text="Ставка").grid(row=2,column=0,columnspan=1)
    p = Entry(newWindow3, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    p.grid(row = 2, column = 1, columnspan = 1)
    p.insert(END,10)
    Label(newWindow3,width=10,text="Тип(a/d)").grid(row=3,column=0,columnspan=1)
    e = Entry(newWindow3, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    e.grid(row = 3, column = 1, columnspan = 1)
    e.insert(END,"a")
    ttk.Button(newWindow3, text="График", command = graph_cred, width = 20).grid(row = 7, column = 0,columnspan=2)
 

def deb_b():
    f = open('deb.txt','w')
    f.close()
    global newWindow4
    def deb_calc():
        deb(ctypes.c_double(float(s.get())),ctypes.c_int(int(t.get())),ctypes.c_double(float(p.get())),ctypes.c_double(float(n.get())),ctypes.c_char(r.get().encode()),ctypes.c_char(k.get().encode()))
        os.system("open deb2.txt")
    try:
        newWindow4.destroy()
    except:pass
    newWindow4 = Toplevel(root)
    newWindow4.title("Deb")
    newWindow4.geometry("200x200")
    newWindow4.attributes('-topmost', 'true')
    newWindow4.attributes('-alpha',0.9)
    Label(newWindow4,width=10,text="Сумма").grid(row=0,column=0,columnspan=1)
    s = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    s.insert(END,1000000)
    s.grid(row = 0, column = 1, columnspan = 1)
    Label(newWindow4,width=10,text="Срок").grid(row=1,column=0,columnspan=1)
    t = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    t.grid(row = 1, column = 1, columnspan = 1)
    t.insert(END,360)
    Label(newWindow4,width=10,text="Ставка").grid(row=2,column=0,columnspan=1)
    p = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    p.grid(row = 2, column = 1, columnspan = 1)
    p.insert(END,10)
    Label(newWindow4,width=10,text="Налог").grid(row=3,column=0,columnspan=1)
    n = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    n.grid(row = 3, column = 1, columnspan = 1)
    n.insert(END,8)
    Label(newWindow4,width=10,text="Пер(m/y)").grid(row=4,column=0,columnspan=1)
    r = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    r.grid(row = 4, column = 1, columnspan = 1)
    r.insert(END,"m")
    Label(newWindow4,width=10,text="Кап(y/n)").grid(row=5,column=0,columnspan=1)
    k = Entry(newWindow4, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    k.grid(row = 5, column = 1, columnspan = 1)
    k.insert(END,"y")
    ttk.Button(newWindow4, text="Список", command = lambda x=0:os.system("open deb.txt"), width = 20).grid(row = 6, column = 0,columnspan=2)
    ttk.Button(newWindow4, text="График", command = deb_calc, width = 20).grid(row = 7, column = 0,columnspan=2)

def x_button():
    global x_min_e,x_max_e,y_min_e,y_max_e,x_entry,newWindow
    try:
        newWindow.destroy()
    except:pass
    newWindow = Toplevel(root)
    newWindow.title("Graph")
    newWindow.geometry("200x150")
    newWindow.attributes('-topmost', 'true')
    newWindow.attributes('-alpha',0.9)
    x_text=Label(newWindow,width=10,text="X").grid(row=0,column=0,columnspan=1)
    x_entry = Entry(newWindow, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    x_entry.insert(END,x_val)
    x_entry.grid(row = 0, column = 1, columnspan = 1)
    x_text_min=Label(newWindow,width=10,text="X min").grid(row=1,column=0,columnspan=1)
    x_min_e = Entry(newWindow, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    x_min_e.grid(row = 1, column = 1, columnspan = 1)
    x_min_e.insert(END,x_min)
    x_text_max=Label(newWindow,width=10,text="X max").grid(row=2,column=0,columnspan=1)
    x_max_e = Entry(newWindow, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    x_max_e.grid(row = 2, column = 1, columnspan = 1)
    x_max_e.insert(END,x_max)
    y_text_min=Label(newWindow,width=10,text="Y min").grid(row=3,column=0,columnspan=1)
    y_min_e = Entry(newWindow, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    y_min_e.grid(row = 3, column = 1, columnspan = 1)
    y_min_e.insert(END,y_min)
    y_text_max=Label(newWindow,width=10,text="Y max").grid(row=4,column=0,columnspan=1)
    y_max_e = Entry(newWindow, width = 10,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
    y_max_e.grid(row = 4, column = 1, columnspan = 1)
    y_max_e.insert(END,y_max)
    ttk.Button(newWindow, text="График", command = graph, width = 20).grid(row = 5, column = 0,columnspan=2)

def numbers():
    bttn_list = ["7", "8", "9",".", 
                "4", "5", "6","+",
                "1", "2", "3","-",
                "(", "0",  ")","*",
                "sin","cos","tan","/",
                "asin","acos","atan","mod",
                "sqrt","ln","log","^"]
    ttk.Button(root, text="Gr", command = x_button, width = 5).grid(row = 1, column = 0)
    ttk.Button(root, text="x", command = lambda x = "x": calc_entry.insert(END, x), width = 5).grid(row = 1, column = 1)  
    ttk.Button(root, text="CE", command = lambda x=0:calc_entry.delete(0, END), width = 5).grid(row = 1, column = 2)              
    ttk.Button(root, text="=", command = c_calc, width = 5).grid(row = 1, column = 3)
    [ttk.Button(root, text=bttn_list[i], command = lambda x = bttn_list[i]: calc_entry.insert(END, x), width = 5).grid(row = 2+i//4, column = i%4) for i in range(len(bttn_list))]
    ttk.Button(root, text="Кредитный", command = cred_b, width = 14).grid(row = 9, column = 0,columnspan=2)
    ttk.Button(root, text="Дебетовый", command = deb_b, width = 14).grid(row = 9, column = 2,columnspan=2)     
root = Tk()
calc_entry = Entry(root, width = 35,bg='white',fg='black',highlightthickness=0,relief='groove',font=("Arial", 15))
calc_entry.grid(row = 0, column = 0, columnspan = 4)
initial_window()
numbers()
x_val=0
x_min=-1
x_max=1
y_min=-1
y_max=1
test = ctypes.CDLL('simple_calc.so')
f=test.calc
f.restype=rpn
f.argtypes=[ctypes.c_char_p,ctypes.c_double]
c = test.cred
c.restype=ctypes.c_double
c.argtypes=[ctypes.c_double, ctypes.c_int, ctypes.c_double,ctypes.c_char]
deb = test.calc_deb
#deb.restype=ctypes.c_double
deb.argtypes=[ctypes.c_double, ctypes.c_int, ctypes.c_double, ctypes.c_double,ctypes.c_char,ctypes.c_char]
root.mainloop()