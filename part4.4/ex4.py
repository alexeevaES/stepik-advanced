""" Напишите программу, которая выводит количество элементов квадратной
матрицы в каждой строке, больших среднего арифметического элементов
данной строки """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

for i in range(n):
    average = 0 # инициализация переменной среднего арифметического
    count = 0   # счетчик количества чисел, больших среднего
    for j in range(n):  # вычисление среднего арифметического
        average += matrix[i][j]
    average = average // n
    for j in range(n):  # подсчет количества элементов, больших среднего
        if matrix[i][j] > average:
            count += 1
    print(count)
