# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
my_list1 = []
minimum = int(input("Введите нижние значение диапазона: "))
maximum = int(input("Введите верхнее значение диапазона: "))
print(my_list := [randint(-10,20) for _ in range(20)])
for i in range(len(my_list)):
    if minimum <= my_list[i] <= maximum:
        my_list1.append(i)
print(my_list1)