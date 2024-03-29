""" На шахматной доске 8х8 стоит конь. Напишите программу, которая отмечает
положение коня на доске и все клетки, которые бьет конь.
Клетку, где стоит конь. отметьте буквой N, клетки, которые бьет конь,
отметьте символами *, остальные клетки заполните точками """

# считываем позицию коня
pos = input()
y = 'abcdefgh'.index(pos[0])
x = '87654321'.index(pos[1])

# создаем шахматное поле с обозначением позиции коня
chess = []
chess = [['.']*8 for _ in range(8)]
chess[x][y] = chess[x][y].replace('.', 'N')

# вычисляем возможные ходы коня
for i in range(8):
    for j in range(8):
        if (abs(i-y) == 2 and abs(j-x) == 1) or \
                (abs(i-y) == 1 and abs(j-x) == 2):
                    chess[j][i] = chess[j][i].replace('.', '*')

for i in range(8):
    print(*chess[i])
