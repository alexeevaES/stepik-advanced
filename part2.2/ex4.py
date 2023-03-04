""" На вход программе подается строка из натуральных чисел.
Из элементов строки формируется список чисел.
Напишите программу циклического сдвига элементов списка вправо,
когда последний элемент становится первым, а остальные сдвигаются
на одну позицию вперед """

numbers = input().split()

# convert elements to int type
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# remember the last digit
last_digit = numbers[-1]

# move elements to right
for i in range(len(numbers)-1, 0, -1 ):
    numbers[i] = numbers[i-1]

# insert last digit into first position
numbers[0] = last_digit

print(*numbers)
