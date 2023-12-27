# подключаем функцию randint() для генерации случайных чисел
from random import randint

# создаем класс Human
class Human:
    # инициализатор класса
    def __init__(self, name, health):
        self._name = name           # имя
        self._health = health       # здоровье
    
    # нанесение урона
    def attack(self, enemy):
        damage = randint(1, 10)     # генерируем значение урона
        print(f'{self._name} наносит персонажу {enemy._name} {damage} урона!')
        enemy.get_damage(damage)    # enemy получает урон в размере damage
    
    # получение урона
    def get_damage(self, damage):
        self._health -= damage      # уменьшаем здоровье на значение damage
        print(f'{self._name} получает {damage} урона! Текущее здоровье - {self._health}.')
    
    # восстановление здоровья
    def healing(self):
        heal = randint(5, 15)       # генерируем значение восстанавливаемого здоровья
        self._health += heal        # восстанавливаем здоровье на значение heal
        print(f'{self._name} восстанавливает {heal} здоровья.')
        print(f'Текущее здоровье - {self._health}.')

# создаем класс Warrior
class Warrior(Human):
    # переопределеляем инициализатор класса
    def __init__(self, name, health, defense):
        super().__init__(name, health)  # вызываем метод __init__() из класса Human
        self._defense = defense         # уровень защиты
    
    # переопределяем метод attack()
    def attack(self, enemy):
        damage = randint(10, 20)    
        print(f'{self._name} наносит персонажу {enemy._name} {damage} урона!')
        enemy.get_damage(damage)    
    
    # переопределяем метод get_damage()
    def get_damage(self, damage):
        # вычисляем итоговое значение урона с учетом защиты
        final_damage = max(damage - self._defense, 0)
        super().get_damage(final_damage)     # вызываем метод get_damage() из класса Human

# создаем класс Warrior
class Archer(Human):
    # переопределеляем инициализатор класса
    def __init__(self, name, health, accuracy, agility):
        super().__init__(name, health)  # вызываем метод __init__() из класса Human
        self._accuracy = accuracy       # меткость
        self._agility = agility         # ловкость

    # переопределяем метод attack()
    def attack(self, enemy):
        # генерируем значение урона с учетом меткости
        damage = randint(15, 25) * self._accuracy
        print(f'{self._name} наносит персонажу {enemy._name} {damage} урона!')
        enemy.get_damage(damage)        
    
    # переопределяем метод get_damage()
    def get_damage(self, damage):
        chance_damage = randint(1, 100)     # генерируем шанс на получение урона
        if self._agility >= chance_damage:  # если ловкость не меньше шанса на получение урона
            print(f'{self._name} увернулся от удара!')
        else:
            super().get_damage(damage)      # вызываем метод get_damage() из класса Human

# создаем по одному экземпляру каждого класса
human = Human(name='Стив', health=80)               
warrior = Warrior(name='Артур', health=120, defense=5)     
archer = Archer(name='Робин', health=90, accuracy=1.15, agility=10)  

human.attack(warrior)   # Стив атакует Артура
warrior.attack(archer)  # Артур атакует Робина
archer.healing()        # Робин залечивает раны