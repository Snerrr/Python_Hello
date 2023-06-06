# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

perviychlen = int(input("Введите первый элемент ар прогрессии: "))
raznost = int(input("Введите разность ар прогрессии: "))
kolelement = int(input("Введите количество элементов ар прогрессии: "))
def arifmprogress(a1: int, d: int, n: int) -> list:
  my_list = []
  for i in range(1, n+1):
    an = a1 + (i-1) * d
    my_list.append(an)
  return my_list
print(arifmprogress(perviychlen, raznost, kolelement))
