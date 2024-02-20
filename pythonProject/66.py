__author__="Arsentyeva N."

print("""Даны целые числа k, m, действительные числа x, y, z. 
При k < m^2, k = m^2, k > m^2 заменить модулем соответственно значения 
x, y или z, а два других значения уменьшить на 0,5.""")

k = int(input())
m = int(input())

x = float(input())
y = float(input())
z = float(input())


if k<m**2:		
	x = abs(x)
	y -= 0.5
	z -= 0.5
elif k == m**2:
	y = abs(y)
	x -= 0.5
	z -= 0.5
else:
	z = abs(z)
	x -= 0.5
	y -= 0.5


print(f"x = {x:.2f}")
print(f"y = {y:.2f}")
print(f"z = {z:.2f}")


# проверка: (1, 2,) -1, -3, -5; x = 1, y = -3.5, z = -5.5 
# проверка: (4, 2,) -1, -3, -5; x = -1.5, y = 3, z = -5.5 
# проверка: (1, 0,) -1, -3, -5; x = -1.5, y = -3.5, z = 5 