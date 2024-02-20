__author__="Arsentyeva N."


import unit

print("""Даны натуральные числа n, a 1...an. Определить количество членов 
ak последовательности a1,...,an: являющихся нечетными числами;""")
n = int(input("Введите n:"))
lst = unit.inputList(n)
k = unit._178a(lst)  # вызов функции 

print(f"Количество нечетных чисел = {k}")