""" На вход подаются два натуральных числа n и m - размерность матрицы.
Напишите программу, которая заполняет матрицу числами от 1 до n*m """

size = [int(num) for num in input().split()]
matrix = []

for i in range(1, size[0]+1):
    temp = []
    for j in range(1, size[1]+1):
        temp.append(i*j)
    matrix.append(temp)

for i in range(size[0]):
    for j in range(size[1]):
        print(str(matrix[i][j]).ljust(3), end='')
    print()
