import numpy as np

def reshape_rows(values, width):
    values = np.array(values, dtype=float)
    padding = (width - values.size % width) % width

    if padding > 0:
        values = np.append(values, [0.0] * padding)

    values = values.reshape(-1, width)
    return values


def block(matrix, rows, columns):
    matrix = np.array(matrix, dtype=float)
    res = matrix[np.ix_(rows, columns)]
    return res


def column_means(matrix):
    matrix = np.array(matrix, dtype=float)
    return np.mean(matrix, axis=0)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

rows = [0, 2]
columns = [1, 2]

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
width = 3

print("Задание 1")
print(reshape_rows(values, width))
print(block(matrix, rows, columns))
print(column_means(matrix))

hours = np.array([8, 9, 10, 11, 12, 13, 14, 15])

print("\nЗадание 2")
print("Третий элемент:", hours[2])
print("Последний элемент:", hours[-1])
print("Элементы с индексами 2-5:", hours[2:6])
print("Каждый второй элемент:", hours[::2])
print("Обратный порядок:", hours[::-1])

temperatures = np.array([
    [12, 14, 13, 15],
    [11, 13, 16, 17],
    [10, 12, 15, 18]
])

print("\nЗадание 3")
print("Форма массива:", temperatures.shape)
print("Число измерений:", temperatures.ndim)
print("Количество элементов:", temperatures.size)
print("Вторая строка, третий столбец:", temperatures[1, 2])
print("Первая строка:", temperatures[0])
print("Последний столбец:", temperatures[:, -1])
print("Первые две строки без первого столбца:")
print(temperatures[:2, 1:])
print("Центральный фрагмент:")
print(temperatures[0:2, 1:3])


matrix = np.arange(1, 26).reshape(5, 5)

print("\nЗадание 4")
print("Исходная матрица:")
print(matrix)

print("Первые три строки:")
print(matrix[:3, :])

print("Последние две строки:")
print(matrix[3:, :])

print("Первые два столбца:")
print(matrix[:, :2])

print("Фрагмент строк 1-3 и столбцов 2-4:")
print(matrix[1:4, 2:5])

print("Правый нижний блок 2x2:")
print(matrix[3:5, 3:5])


vector = np.array([10, 20, 30, 40, 50])

vector[1:4] = 0

small_matrix = np.arange(1, 10).reshape(3, 3)
small_matrix[0, :] = -1
small_matrix[1, 1] = 9

hours = np.array([8, 9, 10, 11, 12, 13, 14, 15])

changed_hours = hours.copy()

changed_hours[2:5] = 99
changed_hours[::2] = -1

print("\nЗадание 5")
print("Исходный массив hours:")
print(hours)

print("Измененный массив changed_hours:")
print(changed_hours)


matrix = np.arange(1, 26).reshape(5, 5)

changed_matrix = matrix.copy()

changed_matrix[1, :] = 0
changed_matrix[:, -1] = -1
changed_matrix[1:4, 1:4] = 100

print("Исходная матрица:")
print(matrix)

print("Измененная матрица:")
print(changed_matrix)


numbers = np.arange(0, 12)

table = numbers.reshape(3, 4)
transposed = table.T

print("\nЗадание 6")
print("Исходный массив:")
print(numbers)

print("Массив table:")
print(table)

print("Транспонированный массив:")
print(transposed)