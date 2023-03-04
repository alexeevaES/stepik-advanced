""" Напишите программу для определения, является ли число произведением
двух чисел из данного набора.
В первой строке подается число n (0 < n < 100) - количество чисел в наборе.
В последующих n строках вводятся целые числа, составляющие набор
(могут повторяться). Затем следует целое число, которое является или
не является произведением двух каких-то чисел набора. """

count = int(input())    # number of digit in the list

numbers = []    # list of digits

# input list
for i in range(count):
    numbers.append(int(input()))

result = int(input())   # the result of multiply of two digits in list

flag = False

# check multiply
for i in range(count-1):
    for j in range(i+1, count):
        if numbers[i] * numbers[j] == result:
            flag = True
            break
if flag:
    print('ДА')
else:
    print('НЕТ')
