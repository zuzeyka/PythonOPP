number = 10 # int
name = "Stepan" # str
surname = "Tarasenko"
b = True # bool
f = 54.34 # float
print(name + surname)

import random
l = [12, True, "test", 54.543, name, True] # создание списка (list)
print(l)

l.append(random.randint(10, 57)) # append добавляет в конец списка новый элемент в ()
print(l) # random.randint генериует случайное число в заданом диапазоне

l.pop(2) # удаляет элемент из списка по индексу
print(l)

l.remove(True) # удаляет первый элемент по значению который найдет в списке
print(l)
# l.clear() # удалить все элементы из списка
print(l)

# логические операторы - операторы которые возвращают как результат тип данных bool or and < > <= >= != ==
"""
True and True = True
True and False = False
False and True = False
False and False = False

True or True = True
True or False = True
False or True = True
False or False = False
"""

if number < 5 and number == 0: # Если сегодня будет дождь то я пойду делать домашку
    print("Hello")
elif number > 5: # если же дождя не будет а будет солнечно, то я пойду гулять
    print("Hello2")
else: # в противном случае я пойду спать
    print("Else")

a = 0
while a < 10: # цикл c условием. Повторяет действия внутри пока условие правдивое
    print("While",)
    a += 1 # a = a + 1

print(l)
for i in range(-10, 40): # for цикл для перебора данных (типов данных с множеством значений)
    print(i) # for будет работать столькор раз сколько есть элементов в перебераемом значении

import functions
functions.Print("Stepan", 15)

import random
for i in range(100):
    print(random.randint(0, 100))


import classes
test = classes.Human("Alex", 180)
# классы 
# класс - пользовательский тип данных который можно описывать функциями и переменными

class Student(classes.Human):
    print("Hello")
    def __init__(self, name, money, height): # init срабатывает только один раз при создании объекта класса
        self.name = name # в поле name назначаю значение переданное в init параметра name 
        self.money = money
        self.height = height
        print("Init") # self - ссылка на текущий объект
    def BuyPizza(self): # можно создавать свои методы
        self.money -= 100 # и взаимодействовасть с полями через self
        print(self.name, "bought a pizza. Now you have", self.money, "uah")

class Car:
    def __init__(self):
        self.color = "red"
        self.model = "BMW"


s = Student('Alex', 200, 180) # создание объекта
s2 = Student("Stepan", 300, 190) # можно создавать несколько объектов
car = Car()
print(car.color, car.model)
s.money = 200 # изменение значения
print(s.name,s.money, s2.name, s2.money)
s.BuyPizza()
s.jump()