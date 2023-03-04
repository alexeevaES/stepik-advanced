""" На вход программе подается строка текста из натуральных чисел.
Из нее формируется список чисел. Напишите программу подсчета количества
чисел, которые больше предшествующего им в этом списке числа,
то есть стоят вслед за меньшим числом """

numbers = input().split()
count = 0

# convert elements to int
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# check
for i in range(len(numbers)-1):
    if numbers[i] < numbers[i+1]:
        count += 1

print(count)
