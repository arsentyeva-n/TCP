__author__="Arsentyeva N."

print("Вычислить cумму ряда с конечным приделом n=50, i=1, 1/i^3")
n = int(input('Введите n:'))
s = 0
for i in range(1, n+1):
	s = s + 1/i**3

print(f"Сумма = {s:.6f}")