# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

from random import randint
my_list = []
kol = 0
n = int(input("Напишите число элементов в массиве: "))
for i in range(n):
    my_list.append(randint(1, n))
print(my_list)
my_list1 = list(set(my_list))
print(my_list1)
for i in range(len(my_list1)):
    for g in range(len(my_list)):
        if my_list1[i] == my_list[g]:
            kol += 1
    print(f"{my_list1[i]}  встречается:  {kol}")
    kol = 0
