#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
n = int(input("Введите число: "))
a = []
for i in range(0,n+1):
    if (2**i < n):
      a+=[2**i]
    else:
       break
       
print(a)