""" На вход программе подается строка текста, содержащая символы.
Из данной строки формируется список. Напишите программу, которая выводит
список, содержащий все возможные подсписки, включая пустой список """

text = input().split()
out_text = [[]]

def chunk(in_list, n, m):
    list_chunked = []
    for j in range(len(in_list)-m):
        list_chunked.append(in_list[j:j+n])
    return list_chunked

for i in range(len(text)):
    mid_text = chunk(text, i+1, i)
   # print(mid_text)
   # print(out_text)
   # print()
    out_text.extend(mid_text)

print(out_text)
