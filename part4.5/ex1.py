""" На вход программе подаются два числа n и m - размерность матрицы.
Создайте матрицу mult размером nxm и заполните её таблицей умножения
по формуле malt[i][j] = [i]*[j] """

n, m = int(input()), int(input())

mult = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        mult[i][j] = i * j

for i in range(n):
    for j in range(m):
        print(str(mult[i][j]).ljust(3), end='')
    print()
