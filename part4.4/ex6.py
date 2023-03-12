""" Напишите программу, которая выводит максимальный элемент из тех,
что находятся в правой и левой четвертях матрицы (диагональ учитывается)"""

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# поиск минимального элемента в исходной матрице
min_matrix = [] # список min по каждой строке
for i in range(n):
    min_matrix.append(min(matrix[i]))
maximum = min(min_matrix)   # min из всей матрицы принимаем за исходно max

# поиск max в обозначенной области матрицы
for i in range(n):
    for j in range(n):
        if ((i >= j) and (i <= n-j-1)) or ((i <= j) and (i >= n-j-1)):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
print(maximum)
