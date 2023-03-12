""" Напишите программу, которая выводит максимальный элемент из тех,
что находятся ниже главной диагонали """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# ищем минимальный элемент в исходной матрице
minimum_matrix = [] # список минимальных элементов по каждой строке
for i in range(n):
    minimum_matrix.append(min(matrix[i]))
maximum = min(minimum_matrix)   # min элемент принимаем за исходно max

# ищем максимальный элемент ниже главной диагонали, включая саму диагональ
for i in range(n):
    for j in range(n):
        if i >= j:
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)
