""" Напишите программу, которая проверяет симметричность квадратной матрицы
относительно главной диагонали """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

flag = True

# проверка симметричности
for i in range(n):
    for j in range(n):
        if matrix[i][j] == matrix[j][i]:
            continue
        else:
            flag = False

if flag:
    print('YES')
else:
    print('NO')
