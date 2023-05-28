# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

from random import randint
x = int(input("Напишите искомое число: "))
n = int(input("Напишите количество элементов в массие: "))
minim = int(input("Напишите минимальное число в массиве: "))
maxim = int(input("Напишите максимальное число в массиве: "))
my_list = []
kol = 0
vse_chisla = []
for i in range(minim , maxim + 1):
    vse_chisla.append(i)         # делаем массив из всех возможных чисел 
for i in range(n):
    my_list.append(randint(minim , maxim))   # делаем массив из случайных чисел
print(my_list)
my_list1 = list(set(my_list))     # только уникальные числа в массиве
my_list1 = sorted(my_list1)       # сортируем массив
print(my_list1)
print()
xxl = max(my_list)       # самое большое число в массиве
low = min(my_list)       # самое маленькое число в массиве
number_malenkie = []     # создаем массив от минимального числа до искомого
number_bolshie = []      # создаем массив от искомого числа до максимального
flag = True
match = []               # создаем массив из ближайшего числа из списка маленького и большого
if x >= xxl:
    print(f"{xxl} - самое близкое число по значению")
if x <= low:
    print(f"{low} - самое близкое число по значению")
if low < x < xxl and flag:
    for i in range(len(my_list1)):
        if x == my_list1[i]:
            print(f"{my_list1[i]} - самое близкое число по значению")
            flag = False
if low < x < xxl and flag:
    for i in range(low, x):
        number_malenkie.append(i)
    number_malenkie = number_malenkie[::-1]
if low < x < xxl and flag:
    for i in range(x +1 , xxl + 1):
        number_bolshie.append(i)
if low < x < xxl and flag:
    for i in range(len(number_malenkie)):
        if len(match) != 1:
          for j in range(len(my_list1)):
              if number_malenkie[i] == my_list1[j]:
                  match.append(number_malenkie[i])
if low < x < xxl and flag:
    for i in range(len(number_bolshie)):
        if len(match) != 2:
          for j in range(len(my_list1)):
              if number_bolshie[i] == my_list1[j]:
                  match.append(number_bolshie[i])
                  break
print()
if len(match) > 0:                   # проверяем, что список не пустой
    distmatch_0 = abs(x - match[0])
    distmatch_1 = abs(x - match[1])
    if distmatch_0 > distmatch_1:
        print(f"{match[1]} - самое близкое число по значению")
    elif distmatch_0 < distmatch_1:
        print(f"{match[0]} - самое близкое число по значению")
    else:
        print(f"{match[0]} и {match[1]} - самые близкие числа по значению")
    
    
                
    
        
        
        
        
    
    
    

