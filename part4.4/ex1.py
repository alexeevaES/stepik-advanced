""" На вход программе подаются два натуральных числа n и m, каждое на
отдельной строке - количество строк и столбцов в матрице. Далее вводятся сами элементы матрицы - слова, каждое на отдельной строке.
Напишите программу, которая сначала считывает элементы матрицы один за другим
затем выводит их в виде матрицы """

n = int(input())
m = int(input())

text = []
matrix = [[''] *m for _ in range(n)]    # инициализация пустой матрицы

# считывание входных строк и добавление в матрицу
for i in range(n):
    for j in range(m):
        matrix[i][j] = input()
for i in range(n):
    print(*matrix[i])   # вывод n-ой строки матрицы