l = [65, 785, 34, 765, 3]
#
#l[6] += l[1]
#print(l[6])

# Исключения в Python это классы которые позволяют выбрасывать и обрабатывать ошибки когда они возникают, а не просто программа будет завершена
print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}" )
try: # с помощью try мы помечаем для себя какой-то небезопастный код, который может вызвать ошибку
    print(number / 0)
except ZeroDivisionError: # с помощью except мы обрабатываем ошибку у каждого типа исключения есть свой класс, который нужно прописывать после except
    print("ZeroDivisionError") # прописывает код который будет выполняться, если ошибка будет возникать
except NameError: # в рамках одного исключения может быть несколько типов исключений и несколько expept
    print("NameError")

<<<<<<< HEAD
print(l)
=======
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
        self.color = "blue"
        self.model = "BMW"


s = Student('Alex', 200, 180) # создание объекта
s2 = Student("Stepan", 300, 190) # можно создавать несколько объектов
car = Car()
print(car.color, car.model)
s.money = 200 # изменение значения
print(s.name,s.money, s2.name, s2.money)
s.BuyPizza()
s.jump()

class Test(classes.Human):
    pass

test = Test()
print(test.name, test.height)
test.name = "Stepan"
test.height = 190
>>>>>>> d4b59f51f25cf365cdb4143cbefb1ff176c679e9
