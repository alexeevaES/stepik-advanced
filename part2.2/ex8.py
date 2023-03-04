""" Камень, ножницы, бумага, ящерица, Спок.
Первая строка - Тимур, вторая - Руслан """

game = ['камень', 'ящерица', 'Спок', 'ножницы', 'бумага']

timur = input()
ruslan = input()

timur_pos = game.index(timur)
ruslan_pos = game.index(ruslan)

if timur_pos == ruslan_pos:
    print('ничья')
elif (timur_pos - ruslan_pos) % 2 == 0:
    if timur_pos > ruslan_pos:
        print('Тимур')
    else:
        print('Руслан')
else:
    if timur_pos > ruslan_pos:
        print('Руслан')
    else:
        print('Тимур')
