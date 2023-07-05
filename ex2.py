#Напишите программу для нахождения максимального числа ягод, которое может 
#собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной 
#во входном файле грядки.
#4
#1234  9
from random import randint


gryadka = []   #рандомно вывели список
for i in range(1, 9):
    gryadka.append(randint(1, 10))
print(gryadka)
maxx = 0
#urojai = gryadka[i] + gryadka[i - 1] + gryadka [(i + 1) % len(gryadka)]
for i in range(len(gryadka)):
    if gryadka[i] + gryadka[i - 1] + gryadka [(i + 1) % len(gryadka)] > maxx:
         maxx = gryadka[i] + gryadka[i - 1] + gryadka [(i + 1) % len(gryadka)]
print(maxx)