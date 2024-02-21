__author__="Arsentyeva N."


import unit
import numpy as np

"""673 Даны действительная матрица размера n x (n + 1) действительные числа a1, ..., an+1, b1, ..., 
bn+1 натуральные числа p, q (p ≤ n, q ≤ n+1). Образовать матрицу размера (n + 1) x (n + 2) вставкой после 
строки с номером р данной матрицы новой строки с элементами a1, ..., an+1 и последующей вставкой после столбца 
с номером q нового столбца с элементами b1, ..., bn+1."""

print("""Задача 673""")
n = int(input("Введите n:"))
p = int(input("Введите место новой строки:"))
q = int(input("Введите место нового столбца:"))

arr = unit.createArray(n)  
print(arr)

# Создаем новую строку с элементами a1, ..., an+1
new_row = np.random.uniform(low=-10.00, high=10.0, size=n+1) # uniform для типа float
#print(new_row)

# Создаем новый столбец с элементами b1, ..., bn+1
new_column = np.random.uniform(low=-10.00, high=10.0, size=n+1)
#print(new_column)

# Вставляем новую строку и новый столбец в матрицу
result_arr = unit._673(arr, new_row, new_column, p, q)

print(result_arr)