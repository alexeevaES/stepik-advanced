""" Напишите программу, которая меняет местами элементы главной и
побочной диагоналей, при этом каждый элемент должен остаться в том же
столбце """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# меняем местами элементы диагоналей
for i in range(n):
    for j in range(n):
        if (i == j):
            matrix[i][j], matrix[n-j-1][j] = \
                    matrix[n-j-1][j], matrix[i][j]
            continue

for i in range(n):
    print(*matrix[i])
