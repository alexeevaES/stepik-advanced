""" Второй вариант решения задачи. Условие см. ex10.py """

n = int(input())    #количество холодильников

data = ''   # строка кода с холодильника
fridge = [] # номера зараженных холодильников
bug_is_here = [0, 0, 0, 0, 0]

# считываем строки кода с холодильников
for i in range(n):
    data = input()
    bug = ['a', 'n', 't', 'o', 'n']    # подпись Антона 
    for j in range(len(bug)):
        if data.find(bug[j]) != -1:
            data = data[data.find(bug[j]):]
            bug[j] = 0
            continue
    if bug == bug_is_here:
        fridge.append(i+1)

print(*fridge)

