"""Дан набор точек на координатной плоскости. Необходимо подсчитать и
вывести количество точек, лежащих в каждой координатной четверти.
В первой строке записано количество точек. Каждая следующая строка
состоит из двух целых чисел - координат точки (x, y),
разделенных символом пробела"""

number_of_dots = int(input())
first_quater = 0
second_quater = 0
third_quater = 0
fourth_quater = 0

# read coordinates for all points
for i in range(number_of_dots):
    coords = input().split()
    # invert list elements from str to int
    for i in range(len(coords)):
        coords[i] = int(coords[i])
    #check
    if coords[0] > 0 and coords[1] > 0:
        first_quater += 1
    elif coords[0] < 0 and coords[1] > 0:
        second_quater += 1
    elif coords[0] < 0 and coords[1] < 0:
        third_quater += 1
    elif coords[0] > 0 and coords[1] < 0:
        fourth_quater += 1

print('Первая четверть: ', first_quater)
print('Вторая четверть', second_quater)
print('Третья четверть', third_quater)
print('Четвертая четверть', fourth_quater)
