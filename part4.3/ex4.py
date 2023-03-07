""" Треугольник Паскаля - бесконечная таблица биномиальных коэффициентов,
имеющая треугольную форму. В этом треугольнике на вершине и по бокам
стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.
На вход программе подается число n.
Напишите программу, которая выводит первые n строк треугольника Паскаля """

from math import factorial

n = int(input())

# функция для вычисления чисел в строке n;
# возвращает список чисел строки n
def pascal(n):
    pascal_list = []
    for k in range(n+1):
        c = int(factorial(n) / (factorial(k) * factorial(n-k)))
        pascal_list.append(c)
    return pascal_list

my_list = [list(pascal(i)) for i in range(n)]

for row in my_list:
    print(*row)
