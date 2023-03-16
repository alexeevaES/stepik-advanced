""" Магическим квадратом порядка n называется квадратная табица,
составленная из всех чисел 1,2,3,...,n^2 так, что суммы по каждому столбцу,
каждой строке и каждой из двух диагоналей равный между собой.
Напишите программу, которая проверяет, является ли заданная квадратная
матрица магическим квадратом """

n = int(input())
matrix = []

# считываем исходную матрицу
for i in range(n):
    temp = [int(num) for num in input().split()]
    matrix.append(temp)

# проверяем, что матрица содержит все числа 1,2,3,...,n^2
size = n*n  # количество проверяемых цифр - nxn
flag = True # флаг проверки
# преобразуем исходную матрицу в одномерный список для проверки
check = []
for i in range(n):
    check.extend(matrix[i])
# выполняем проверку
for i in range(1, size+1):
    if i not in check and check.count(i) != 1:
        flag = False
        break

# если проверка не пройдена, завершаем выполнение программы
if not flag:
    print('NO')
else:   # если проверка пройдена
    check_matrix = []   # список для хранения сумм
    check_sum = 0   # переменная для подсчета суммы и записи в список
    # считаем суммы диагоналей
    for i in range(n):
        for j in range(n):
            if i == j:
                check_sum += matrix[i][j]
    # добавляем сумму главной диагонали в список и берем в качестве исходной
    check_matrix.append(check_sum)
    # считаем сумму побочной диагонали
    check_sum = 0
    for i in range(n):
        for j in range(n):
            if i == n-j-1:
                check_sum += matrix[i][j]
    check_matrix.append(check_sum)
    # считаем суммы по строкам
    for i in range(n):
        check_matrix.append(sum(matrix[i]))
    # считаем суммы по столбцам
    for i in range(n):
        check_sum = 0
        for j in range(n):
            check_sum += matrix[j][i]
        check_matrix.append(check_sum)
    if check_matrix.count(check_matrix[0]) == len(check_matrix):
        print('YES')
    else:
        print('NO')
