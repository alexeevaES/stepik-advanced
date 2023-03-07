""" На вход программе подается строка, содержащая символы.
Напишите программу, которая упаковывает последовательности одинаковых
символов заданной строки в подсписки """

text = input().split()
text_list = []

text_list.append(list(text[0])) # добавляем первый элемент входной строки
                                # чтобы начать цикл со второго элемента

for i in range(1, len(text)):
    if text[i] != text[i-1]:
        text_list.append(list(text[i]))
    else:
        text_list[-1].append(text[i])

print(text_list)
