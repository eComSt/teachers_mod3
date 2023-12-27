from tkinter import *
from time import sleep
def pressed():
    print(name.get(), selected.get(),age.get(),check_state.get())
    label['text'] = 'Спасибо, что прошли анкету!'
window = Tk()
window.title("Анкета")
window.geometry('700x500+200+150')
label = Label(text="Расскажите о себа", font=("Arial", 20))
label.place(x=200, y=10)
about = Message(text='Мы рады приветствовать вас в нашей анкете дружбы! Пожалуйста, отвечайте на вопросы честно, вся информация останется между нами.', font=('Arial', 14), width=680)
about.configure(justify=CENTER)
about.place(x=5, y=70)
name = Entry(width=30)
name.place(x=70, y=155)
label_name = Label(text="ФИО", font=('Arial', 14))
label_name.place(x=5,y=155)
selected = IntVar()
rad1 = Radiobutton(text="Мужской", value=1, variable=selected, font=('Arial', 14))
rad2 = Radiobutton(text="Женский", value=2, variable=selected, font=('Arial', 14))
rad1.place(x=10, y=200)
rad2.place(x=100, y=200)
label_age = Label(text="Возраст", font=('Arial', 14))
label_age.place(x=5, y=250)
age = Spinbox(from_=0, to=100, width=5)
age.place(x=10, y=300)
check_state = IntVar()
check = Checkbutton(text="Запомнить меня", variable=check_state, font=('Arial', 14))
check.place(x=10, y=350)
btn = Button(text="Отправить", command=pressed, font=('Arial', 14),bg = 'green', fg = 'white')
btn.place(x=100,y=400)
# while True:
#     window.update()
#     label['text'] += 'Hello'
#     sleep(1)
window.mainloop()
