l = [65, 785, 34, 765, 3]
#
#l[6] += l[1]
#print(l[6])

# Исключения в Python это классы которые позволяют выбрасывать и обрабатывать ошибки когда они возникают, а не просто программа будет завершена
print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}" )

f = open("test.txt", "w") # w - запись в файл, a - дозапись в файл, r - чтение из файла
f.write("Hello World") # запись в файл
f.close() # закрытие файла

f = open("test.txt", "a") # w - запись в файл, a - дозапись в файл, r - чтение из файла
f.write("123") # запись в файл
f.close() # закрытие файла

f = open("test.txt", "r")
print(f.read()) # чтение из файла
f.close()

import datetime
a = 0
log = open("log.txt", "w")
while a < 100:
    try: # с помощью try мы помечаем для себя какой-то небезопастный код, который может вызвать ошибку
        print(100 / a)
        if a % 2 == 0:
            name += 5
    except ZeroDivisionError: # с помощью except мы обрабатываем ошибку у каждого типа исключения есть свой класс, который нужно прописывать после except
        log.write(f"[{datetime.datetime.now()}] a = {a} - ZeroDivisionError\n") # прописывает код который будет выполняться, если ошибка будет возникать
    except NameError: # в рамках одного исключения может быть несколько типов исключений и несколько expept
        log.write(f"[{datetime.datetime.now()}] a = {a} - NameError\n")
    else:
        log.write(f"[{datetime.datetime.now()}] a = {a} - no problems\n")
    a += 1
    if a == 100:
        break
    print(a)
else: # для while можно прописать else который будет выполняться только в случае когда условие в цикле while вернуло False
    print("End") # else не будет выполняться если в середине цикла сработал break
