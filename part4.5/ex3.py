""" Напишите программу, которая меняет местами столбцы в матрице.
i, j - номера столбцов, подлежащих обмену """

n, m = int(input()), int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# считываем i, j
cols = [int(num) for num in input().split()]

# меняем столбцы местами
for i in range(n):
    matrix[i][cols[0]], matrix[i][cols[1]] = \
    matrix[i][cols[1]], matrix[i][cols[0]]

for i in range(n):
    print(*matrix[i])
