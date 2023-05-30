# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств

from random import randint
my_list = []
my_list_1 = []
my_list_peresechenia = []
n = int(input("Напишите число элементов в 1 массиве: "))
m = int(input("Напишите число элементов во 2 массиве: "))
for i in range(n):
    my_list.append(randint(-10, 20))
for i in range(m):
    my_list_1.append(randint(-20, 40))
my_list = sorted(set(my_list))
for i in range(len(my_list)):
    if my_list[i] in my_list_1:
        my_list_peresechenia.append(my_list[i])
print(my_list_peresechenia)

