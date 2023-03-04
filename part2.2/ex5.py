""" На вход программе подается строка текста, содержащая натуральные числа,
расположенные по неубыванию.
Из строки формируется список чисел.
Напишите программу для подсчета количества разных элементов в списке """

input_numbers = [] # вводимая строка
numbers = [] # список из неповторяющихся чисел

input_numbers = input().split()

for i in range(len(input_numbers)):
    if input_numbers[i] not in numbers:
        numbers.append(input_numbers[i])

print(len(numbers))
