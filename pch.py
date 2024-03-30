

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
    def __str__(self):
        return f"Car:\nColor: {self.color}\nModel: {self.model}"

car = Car()
print(car)

s = Student('Alex', 200, 180) # создание объекта
s2 = Student("Stepan", 300, 190) # можно создавать несколько объектов
s.money = 200 # изменение значения
print(s.name,s.money, s2.name, s2.money)
s.BuyPizza()
s.jump()

class Test(classes.Human):
    pass

test = Test()
print(test.name, test.height)
test.name = "Stepan"