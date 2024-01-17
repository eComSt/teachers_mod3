from tkinter import *
window = Tk()

print(window.winfo_screenwidth(),window.winfo_screenheight())
window.geometry("350x300")
for c in range(2): 
    window.columnconfigure(index=c,weight=1)
    window.rowconfigure(index=c,weight=1)
btn1 = Button(window, text="Кнопка 1", font=("Arial",15))
# btn1.place(x=10,y=10)
btn1.grid(row=0,column = 0)
btn2 = Button(window, text="Кнопка 2", font=("Arial",15))
btn2.grid(row=1,column = 1,columnspan=2,rowspan=2)
btn3 = Button(window, text="Кнопка 3", font=("Arial",15))
btn3.grid(row=2,column = 2)
window.mainloop()
    