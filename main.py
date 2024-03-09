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