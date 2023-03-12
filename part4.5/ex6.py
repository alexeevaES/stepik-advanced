""" Напишите программу, которая зеркально отображает ее элементы
относительно горизонтальной оси симметрии """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# отображаем матрицу
for i in range(n//2):   #достаточно пройти до середины матрицы
    matrix[i], matrix[n-i-1] = matrix[n-i-1], matrix[i]

for i in range(n):
    print(*matrix[i])
