""" На вход программе подается строка текста из натуральных чисел.
Из элементов строки формируется список чисел.
Напишите программу, которая меняет местами соседние элементы списка.
Если в списке нечетное количество элементов, то последний остается
на своем месте """

numbers = input().split()

# convert elements to int
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# swap elements
if len(numbers) % 2 == 0:
    for i in range(0, len(numbers)-1, 2):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
else:
    for i in range(0, len(numbers)-2, 2):
        numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

print(*numbers)
