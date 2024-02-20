__author__="Arsentyeva N."


import unit
import numpy as np

print("""Задача 673""")
n = int(input("Введите n:"))
p = int(input("Введите место новой строки:"))
q = int(input("Введите место нового столбца:"))

arr = unit.createArray(n)  #
print(arr)

# Создаем новую строку с элементами a1, ..., an+1
new_row = np.random.randint(-10, 11, size=n+1)
#print(new_row)

# Создаем новый столбец с элементами b1, ..., bn+1
new_column = np.random.randint(-10, 11, size=n+1)

#print(new_column)
# Вставляем новую строку и новый столбец в матрицу
result_arr = unit._673(arr, new_row, new_column, p, q)

print(result_arr)