# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
Massiv_1 = [1, 2, 45, 6, 8, 33, 21, 9, 12, 35]
min_number = int(input("Введите минимум диапазона: "))
max_number = int(input("Введите максимум дипозона: "))
for i in range(len(Massiv_1)):
    if min_number <= Massiv_1[i] <= max_number:
        print(i) 