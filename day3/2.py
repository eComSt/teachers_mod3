# # Работа с Custom Tkinter I

# # Работа с простыми виджетами

# from customtkinter import *

# # создаем и настраиваем главное окно
# window = CTk()
# window.title('Мое окно')
# window.geometry('400x300')

# # задаем сеточную конфигурацию окна
# window.grid_columnconfigure((0), weight=1)
# window.grid_rowconfigure((0, 1, 2, 3), weight=1)

# # создаем и размещаем однострочный текст
# label = CTkLabel(window, text='Пример текста в CustomTkinter')
# label.grid(row=0, column=0)
# # меняем размер шрифта однострочного текста
# label.cget('font').configure(size=20)

# # Фрейм - дополнительная область внутри окна для структурирования виджетов
# # Создаем и размещаем фрейм для группировки чек-боксов
# checkbox_frame = CTkFrame(window)
# checkbox_frame.grid(row=1, column=0, padx=10, pady=10, sticky='nswe')
# # задаем сеточную конфигурацию для фрейма
# checkbox_frame.grid_columnconfigure((0), weight=1)
# checkbox_frame.grid_rowconfigure((0, 1), weight=1)
# # создаем и размещаем 2 чек-бокса
# checkbox_1 = CTkCheckBox(checkbox_frame, text='Вариант 1')
# checkbox_1.grid(row=0, column=0)
# checkbox_2 = CTkCheckBox(checkbox_frame, text='Вариант 2')
# checkbox_2.grid(row=1, column=0)

# # создаем и размещаем стандартную кнопку
# button = CTkButton(window, text='Кнопка', fg_color='blue')
# button.grid(row=3, column=0, padx=20, pady=20, sticky='we')

# # запускаем цикл обработки событий
# window.mainloop()

# -------------------------------------------------------

# Создание собственного виджета "Спинбокс"

# Cпинбокс будет состоять из 4 компонентов:
# - фрейм для группировки составляющих спинбокса
# - 2 стандартные кнопки для увеличения и уменьшения значения на 1
# - лейбл для отображения текущего числа

from customtkinter import *

# устанавливаем зеленую цветовую тему
set_default_color_theme('green')

# функция для увеличения значения на 1
def add():
    label.configure(text=str(int(label.cget('text')) + 1))

# функция для уменьшения значения на 1
def sub():
    label.configure(text=str(int(label.cget('text')) - 1))

# создаем и настраиваем главное окно
window = CTk()
window.geometry('300x300')
# задаем сеточную конфигурацию окна
window.grid_columnconfigure((0), weight=1)
window.grid_rowconfigure((0), weight=1)

width = 200     # ширина фрейма
height = 50     # высота фрейма

# создаем и размещаем фрейм
frame = CTkFrame(window, width=width, height=height)
frame.grid(row=0, column=0)

# создаем и размещаем кнопку для уменьшения значения
sub_button = CTkButton(frame, text="-", width=height, height=height, command=sub,bg_color='red',border_color='yellow')
sub_button.grid(row=0, column=0, padx=3, pady=3)

# создаем и размещаем лейбл для отображения текущего числа 
label = CTkLabel(frame, width=(width - height*2), height=height, corner_radius=25, fg_color='grey', text='0')
label.grid(row=0, column=1,  padx=3, pady=3)

# создаем и размещаем кнопку для увеличения значения
add_button = CTkButton(frame, text="+", width=height, height=height, command=add)
add_button.grid(row=0, column=2, padx=3, pady=3)

# запускаем цикл обработки событи
window.mainloop()


