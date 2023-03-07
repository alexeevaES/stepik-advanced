""" На вход программе подается строка с символами и строка с числом.
Из первой строки формируется список.
Рализуйте функцию chunked(), которая принимает на вход список и число,
задающее размер чанка (куска), а возвращает список из чанков
указанной длины """

text = input().split()
chunk = int(input())

def chunked(char, n):
    list_chunked = []
    for i in range(0, len(char), n):
        list_chunked.append(char[i:(i+n)])
    return list_chunked

print(chunked(text, chunk))
