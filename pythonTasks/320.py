__author__="Arsentyeva N."


import unit

print("""Задача 320, вычислить выражение""")
n = int(input("Введите n:"))
m = int(input("Введите m:"))
s = unit._320(n,m)  # вызов функции вычисления выражения из модуля unit

print(f"Сумма = {s:.6f}")