""" Следом квадратной матрицы называется сумма элементов главной диагонали.
Напишите программу, которая выводит след заданной матрицы """

n = int(input())
matrix = []
sled = 0

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# высчитываем след матрицы
for i in range(n):
    sled += matrix[i][i]

print(sled)
