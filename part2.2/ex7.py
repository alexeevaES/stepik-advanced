""" Камень, ножницы, бумага. Первая строка - Тимур, вторая - Руслан """

game = []

game.append(input())
game.append(input())

if game[0] == game[1]:
    print('ничья')
elif (game[0] == 'камень' and game[1] == 'бумага') or \
        (game[0] == 'бумага' and game[1] == 'ножницы') or \
        (game[0] == 'ножницы' and game[1] == 'камень'):
            print('Руслан')
else:
    print('Тимур')
