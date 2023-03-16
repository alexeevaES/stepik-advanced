""" Напишите программу, которая переворачивает квадратную матрицу чисел
на 90 градусов по часовой стрелке """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# создадим пустую матрицу размерностью n
new_matrix = [[0]*n for _ in range(n)]

# переворачиваем матрицу
for i in range(n):
    for j in range(n):
        new_matrix[i][j] = matrix[n-j-1][i]
print()

for i in range(n):
    print(*new_matrix[i])
