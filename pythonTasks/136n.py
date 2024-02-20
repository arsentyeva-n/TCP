__author__="Arsentyeva N."

import unit

print("Даны натуральное число n, действительные числа a1,..., an. Вычислить:")
n = int(input("Введите n:"))
lst = unit.inputList(n)  # ввод значений
s = unit.sum136n(lst)  # вызов функции sum

print(f"Сумма = {s:.6f}")
print(unit.sum136n.__doc__) # вывод коментариев функции