""" На вход программе подаются два натуральных числа n и m -
размерность матрицы. Заполните ее символами . и * в шахматном порядке.
В левом верхнем углу должна стоять точка. При выводе разделить элементы
пробелом """

size = [int(num) for num in input().split()]
matrix = []

for i in range(size[0]):
    temp = []
    for j in range(1, size[1]+1):
        if (i-j) % 2 == 0:
            temp.append('*')
        else:
            temp.append('.')
    matrix.append(temp)
for i in range(size[0]):
    print(*matrix[i], sep=' ')
