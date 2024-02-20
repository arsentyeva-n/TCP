__author__ = "Arsentyeva N."

from math import sqrt
import numpy as np

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


# Создаем матрицу из нулей
def createArray(n:int):
    """Создание матрицы размера nхn+1 с нулями"""
    random_array = np.zeros((n, n+1))
    return random_array

def _673(matrix: bytearray, new_row: list, new_column: list, p:int, q:int):
    """Решение 673 задачи, вставка нового столбца и строки в исходную матрицу"""
    new_matrix = np.insert(matrix, p, new_row, axis=0)
    new_matrix = np.insert(new_matrix, q, new_column, axis=1)
    return new_matrix


def test673():
    matrix = createArray(3)
    new_row = np.array([[1, 2, 3, 4]])
    new_column = np.array([[1, 2, 3, 4]])

    # Проверка вставки в начало матрицы
    p = 0
    q = 0
    test_matrix = [[1,1,2,3,4],
                   [2,0,0,0,0],
                   [3,0,0,0,0],
                   [4,0,0,0,0]]
    result_matrix = _673(matrix, new_row, new_column, p, q)
    assert np.array_equal(test_matrix,result_matrix)

    matrix = createArray(3)

    # Проверка вставки в конец матрицы
    p = 3
    q = 4
    test_matrix = [[0, 0, 0, 0, 1],
                   [0, 0, 0, 0, 2],
                   [0, 0, 0, 0, 3],
                   [1, 2, 3, 4, 4]]
    result_matrix = _673(matrix, new_row, new_column, p, q)
    assert np.array_equal(test_matrix, result_matrix)


    print("Тест успешно пройден!")


test673()
sumTest()
test178a()
test320()