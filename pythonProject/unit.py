__author__ = "Arsentyeva N."

from math import sqrt


# Ввод значений
def inputList(n: int):
    """Ввод n значений"""
    lst = []
    for i in range(1, n + 1):
        a = float(input(f"a{i}:"))  # ввод значений a1,..an
        lst.append(a)
    return lst


# 136н задача
def sum136n(lst: list):
    """Вычисление суммы выражения из задачи 136н"""
    s = 0
    for e in lst:
        s = s + (sqrt(abs(e)) - e) ** 2
    return s


def sumTest():
    """Тест задачи 136н"""
    assert sum136n([1, 2, 3, 4, 5]) == 13.590161130096458
    assert sum136n([10, 20, 30]) == 889.2354740935496
    assert sum136n([-10, -3, 10]) == 242.39230484541326
    print("Тест успешно пройден!")


# 178а задача
def _178a(lst: list):
    """Определение количества членов ak последовательности a1,...,an: являющихся нечетными числами"""
    k = 0
    for e in lst:
        if e % 2 == 1:
            k += 1
    return k


def test178a():
    """Тест задачи 178a"""
    assert _178a([1, 2, 3, 4, 5]) == 3
    assert _178a([10, 20, 30]) == 0
    assert _178a([-10, -3, 10, 2, 5, 1, 1, 1]) == 5
    print("Тест успешно пройден!")


# 320 задача
def _320(n: int, m: int):
    """Вычисление суммы ряда из задачи 320"""
    s = 0
    for k in range(1, n + 1):
        for l in range(1, m + 1):
            s += k ** 3 * ((k - l) ** 2)
    return s


def test320():
    """Тест задачи 320"""
    assert _320(10,15) == 983455.000000
    assert _320(10,10) == 586245.000000
    assert _320(11,5) == 949740.000000
    print("Тест успешно пройден!")

# sumTest()
# test178a()
#test320()