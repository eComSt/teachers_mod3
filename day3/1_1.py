# Классы с Tkinter

# Игра "Камень, ножницы, бумага"
# Камень -> Ножницы, Ножницы -> Бумага, Бумага -> Камень

# 1. Механика игры (класс Game)
# 2. Графический интерфейс (класс GUI)

from tkinter import *
from random import choice

# класс механики игры
class Game:
    # инициализатор класса
    def __init__(self):
        self.win = 0    # кол-во побед
        self.lose = 0   # кол-во поражений
        self.draw = 0   # сколько раз выпала ничья
        self.moves = ['Камень', 'Ножницы', 'Бумага']    # возможные ходы
    
    # метод для обработки хода игрока и получения результата
    def move_result(self, user_choice):
        # генерируем ход игры
        comp_choice = choice(self.moves)
        # проверка на ничью
        if user_choice == comp_choice:
            self.draw += 1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nНичья'
        # проверка на победу игроком
        elif user_choice == 'Камень' and comp_choice == 'Ножницы' or \
                user_choice == 'Ножницы' and comp_choice == 'Бумага' or \
                user_choice == 'Бумага' and comp_choice == 'Камень':
            self.win += 1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПобеда'
        # проверка на проигрыш игрока
        else:
            self.lose += 1
            return f'Ход игрока: {user_choice}\nХод компьютера: {comp_choice}\nПроигрыш'
    
    # метод для вывода информации на экран
    def show_info(self):
        return f'Победы: {self.win}\nПроигрыши: {self.lose}\nНичьи: {self.draw}'

# класс графического интерфейса
class GUI:
    # инициализатор класса
    def __init__(self):
        self.window = Tk()
        self.window.geometry('500x300')
        self.window.title('Камень, ножницы, бумага')
        self.game = Game()
        # заполняем окно виджетами
        self.startUI(self.window)
        # запускаем цикл обработки событий
        self.window.mainloop()
    
    # метод для заполнения главного окна виджетами
    def startUI(self, window):
        # задаем сеточную систему окна (3 ряда, 3 колонки)
        for c in range(3): window.columnconfigure(index=c, weight=1)
        for r in range(3): window.rowconfigure(index=r, weight=1)
        # создаем и размещаем 3 кнопки
        self.btn1 = Button(window, text='Камень', font=('Arial', 15),
                           command=lambda: self.btn_click('Камень'))
        self.btn2 = Button(window, text='Ножницы', font=('Arial', 15),
                           command=lambda: self.btn_click('Ножницы'))
        self.btn3 = Button(window, text='Бумага', font=('Arial', 15),
                           command=lambda: self.btn_click('Бумага'))
        self.btn1.grid(row=2, column=0)
        self.btn2.grid(row=2, column=1)
        self.btn3.grid(row=2, column=2)
        # создаем и размещаем подпись с результатом игры
        self.lbl = Label(window, text='Начало игры!', font=('Arial', 20))
        self.lbl.grid(row=1, column=0, columnspan=3)
        # создаем и размещаем подпись с информацией об игре
        self.lbl2 = Label(window, justify='left', font=('Arial', 13), text=self.game.show_info())
        self.lbl2.grid(row=0, column=0)
    # метод обработки нажатий на кнопки
    def btn_click(self, user_choice):
        self.lbl['text'] = self.game.move_result(user_choice)
        self.lbl2['text'] = self.game.show_info()

# создаем экземпляр класса GUI() и запускаем игру
app = GUI()
    
