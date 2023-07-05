#Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
#Выдать без повторений в порядке возрастания все те числа, которые встречаются
#в обоих наборах.Пользователь вводит 2 числа. n — кол-во элементов первого множества. 
#m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

from random import randint


n = int(input())
m = int(input())
arr_n = []   #рандомно вывели список
for i in range(1, n):
    arr_n.append(randint(1, 10))
#print(arr_n)
my_set_n = set(arr_n)
#print(my_set_n)
arr_m = []   
for i in range(1, m):
    arr_m.append(randint(1, 10))
my_set_m = set(arr_m)
my_set_m = set(arr_m)

print(arr_n)
print(arr_m)
print(my_set_n)
print(my_set_m)


cross = sorted(my_set_n.intersection(my_set_m))
print(cross)