""" На вход программе подаются два натуральных числа n и m - размерность
матрицы. Затем n строк по m целых чисел в каждой, разделенных пробелом.
Напишите программу, которая находит индексы первого max элемента"""

n, m = int(input()), int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# найдем максимальные элементы в каждой из строк
max_matrix = []
for i in range(n):
    max_matrix.append(max(matrix[i]))

# максимальный элемент из всей матрицы
maximum = max(max_matrix)

# ищем индексы максимального элемента
pos_i = max_matrix.index(maximum)
pos_j = matrix[pos_i].index(maximum)

print(pos_i, pos_j)
