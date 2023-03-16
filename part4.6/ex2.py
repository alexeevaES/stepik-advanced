""" На вход программе подается натуральное число n - размерность
квадратной матрицы. Напишите программу, которая выводит матрицу:
    числа на побочной диагонали равны 1
    числа выше этой диагонали равны 0
    числа ниже этой диагонали равны 2 """

n = int(input())
matrix = []

for i in range(n):
    temp = []
    for j in range(n):
        if i < n-j-1:
            temp.append(0)
        elif i == n-j-1:
            temp.append(1)
        else:
            temp.append(2)
    matrix.append(temp)

for i in range(n):
    print(*matrix[i], sep=' ')
