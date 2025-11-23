# Вариант 1.
# 1. Вычислить сумму и число положительных элементов матрицы A[N,
# N], находящихся над главной диагональю.
n = int (input('Введите ширину матрицы '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)
f = []
for i in range(n):
    for j in range(n):
        if i < j:
            if A[i][j] > 0:
                f.append(A[i][j])

print('Сумма положит элементов', sum(f),
      'Кол положит элементов', len(f))

# 2. Дана матрица B[N, М]. Найти в каждой строке матрицы
# максимальный и минимальный элементы и поменять их с первым и
# последним элементами строки соответственно.
n = int(input('Введите ширину матрицы '))
m = int(input('Введите высоту матрицы '))

B = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    B.append(b)

for j in range(n):
    row = B[j]

    max_idx = row.index(max(row))
    min_idx = row.index(min(row))

    first = row[0]
    last = row[m - 1]
    maximum = row[max_idx]
    minimum = row[min_idx]

    row[max_idx] = first
    row[0] = maximum

    row[min_idx] = last
    row[m - 1] = minimum

for i in range(n):
    for j in range(m):
        print(B[i][j], end=' ')
    print()

# Вариант 2.
# 1. Дана целая квадратная матрица n-го порядка. Определить,
# является ли она магическим квадратом, т. е. такой матрицей, в которой
# суммы элементов во всех строках и столбцах одинаковы.
n = int(input('Введите ширину матрицы '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

etalon_summi = sum(A[0])
magic = all(sum(row) == etalon_summi for row in A) and \
        all(sum(A[i][j] for i in range(n)) == etalon_summi for j in range(n)) and \
        sum(A[i][i] for i in range(n)) == etalon_summi and \
        sum(A[i][n-1-i] for i in range(n)) == etalon_summi

print('Является' if magic else 'Не является')

# 2. Дана прямоугольная матрица A[N, N]. Переставить первый и
# последний столбцы местами и вывести на экран.
n = int (input('Введите ширину матрицы '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [',i,',',j,'] элемент')
        b.append(int(input()))
    A.append(b)

for i in range(n):
    A[i][0], A[i][n - 1] = A[i][n - 1], A[i][0]

for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()

# Вариант 3.
# 1. Определить, является ли заданная целая квадратная матрица n-го
# порядка симметричной (относительно главной диагонали).
n = int(input('Введите ширину матрицы '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

symmetric = all(A[i][j] == A[j][i] for i in range(n) for j in range(i + 1, n))

print('Симметрична' if symmetric else 'Не симметрична')

# 2. Дана вещественная матрица размером n х m. Переставляя ее
# строки и столбцы, добиться того, чтобы наибольший элемент (или один
# из них) оказался в верхнем левом углу.
n = int(input('Введите ширину матрицы '))
m = int(input('Введите высоту матрицы '))

B = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    B.append(b)

max_val = B[0][0]
max_i, max_j = 0, 0
for i in range(n):
    for j in range(m):
        if B[i][j] > max_val:
            max_val = B[i][j]
            max_i, max_j = i, j

# Поменять строки max_i с первой строкой
B[0], B[max_i] = B[max_i], B[0]

# Поменять столбец max_j с первым столбцом
for i in range(n):
    B[i][0], B[i][max_j] = B[i][max_j], B[i][0]

for i in range(n):
    for j in range(m):
        print(B[i][j], end=' ')
    print()

# Вариант 4.
# 1. Дана прямоугольная матрица. Найти строку с наибольшей и строку
# с наименьшей суммой элементов. Вывести на печать найденные строки и
# суммы их элементов.
n = int(input('Введите ширину матрицы '))
m = int(input('Введите высоту матрицы '))

B = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    B.append(b)

prevmin = sum(B[0])
prevmax = sum(B[0])
min_idx, max_idx = 0, 0

for j in range(1, n):  # начинаем с 1, т.к. 0 уже учли
    current_sum = sum(B[j])
    if current_sum > prevmax:
        prevmax = current_sum
        max_idx = j
    if current_sum < prevmin:
        prevmin = current_sum
        min_idx = j

# Вывод
print('Минимальная строка:', B[min_idx], 'Сумма:', prevmin)
print('Максимальная строка:', B[max_idx], 'Сумма:', prevmax)

# 2. Дана квадратная матрица A[N, N], Записать на место
# отрицательных элементов матрицы нули, а на место положительных —
# единицы.
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде.
n = int(input('Введите ширину матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            A[i][j] = 1 # на место положительных единицы.
        elif A[i][j] < 0:
            A[i][j] = 0 # на место отрицательных нули.

for i in range(n):
    for j in range(n):
        if j <= i:  # Выводим только элементы на и ниже диагонали, треугольник
            print(A[i][j], end=' ')
        else:
            print(' ', end=' ')
    print()

# Вариант 5.
# 1. Упорядочить по возрастанию элементы каждой строки матрицы
# размером n х m.
n = int(input('Введите ширину матрицы '))
m = int(input('Введите высоту матрицы '))

B = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    B.append(b)

for i in range(n):
    B[i].sort()  # Сортировка по возрастанию

for i in range(n):
    for j in range(m):
        print(B[i][j], end=' ')
    print()

# 2. Дана действительная матрица размером n х m, все элементы
# которой различны. В каждой строке выбирается элемент с наименьшим
# значением. Если число четное, то заменяется нулем, нечетное -
# единицей. Вывести на экран новую матрицу.
n = int(input('Введите ширину матрицы '))
m = int(input('Введите высоту матрицы '))

B = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    B.append(b)

for i in range(n):
    minimum = min(B[i])
    minindex = B[i].index(minimum)
    B[i][minindex] = 1 if (minimum % 2 != 0) else 0

for i in range(n):
    for j in range(m):
        print(B[i][j], end=' ')
    print()

# Вариант 6.
# 1. Дана целочисленная квадратная матрица. Найти в каждой строке
# наибольший элемент и в каждом столбце наименьший. Вывести на
# экран.
n = int(input('Введите ширину матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

for i in range(n):
    print('Наибольший элемент строки',i,'=', max(A[i]))
for i in range(n):
    f = []
    for j in range(n):
        f.append(A[j][i])
    print('Наименьший элемент столбца', i, '=', min(f))

# 2. Дана действительная квадратная матрица порядка N (N —
# нечетное), все элементы которой различны. Найти наибольший элемент
# среди стоящих на главной и побочной диагоналях и поменять его
# местами с элементом, стоящим на пересечении этих диагоналей.
n = int(input('Введите нечётный размер матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

diagonal_elements = []

# Главная диагональ
for i in range(n):
    diagonal_elements.append((A[i][i], i, i))

# Побочная диагональ
for i in range(n):
    j = n - 1 - i
    if i != j:
        diagonal_elements.append((A[i][j], i, j))

# Максимальный элемент среди диагональных
max_val, max_i, max_j = max(diagonal_elements, key=lambda x: x[0])

center = n // 2

A[max_i][max_j], A[center][center] = A[center][center], A[max_i][max_j]

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

# Вариант 7.
# 1. Квадратная матрица, симметричная относительно главной
# диагонали, задана верхним треугольником в виде одномерного массива.
# Восстановить исходную матрицу и напечатать по строкам.
n = int(input('Введите ширину матрицы: '))
treugoln = []
print('Введите элементы верхнего треугольника:')
for i in range(n * (n + 1) // 2):
    treugoln.append(int(input()))

A = [[0] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(i, n):
        A[i][j] = treugoln[k]
        A[j][i] = treugoln[k]  # симметричный элемент
        k += 1

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

# 2. Для заданной квадратной матрицы сформировать одномерный
# массив из ее диагональных элементов. Найти след матрицы,
# просуммировав элементы одномерного массива. Преобразовать
# исходную матрицу по правилу: четные строки разделить на полученное
# значение, нечетные оставить без изменения.
n = int(input('Введите ширину матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

diagonal = [A[i][i] for i in range(n)]

sum_diag = sum(diagonal)

for i in range(n):
    if i % 2 == 0:  # чётная строка
        for j in range(n):
            A[i][j] /= sum_diag

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

# Вариант 8.
# 1. Задана матрица порядка n и число к. Разделить элементы k-й
# строки на диагональный элемент, расположенный в этой строке.
n = int(input('Введите ширину матрицы: '))
k = int(input('Введите номер строки (от 0 до ' + str(n - 1) + '): '))

A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

diag_element = A[k][k]

for j in range(n):
    A[k][j] /= diag_element

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

# 2. Задана квадратная матрица. Получить транспонированную
# матрицу (перевернутую относительно главной диагонали) и вывести на
# экран.
n = int(input('Введите ширину матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

for i in range(n):
    for j in range(n):
        print(A[j][i], end=' ')  # i и j поменяли местами
    print()

# Вариант 9.
# 1. Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
n = int(input('Введите размер матрицы: '))
k = int(input('Введите число k: '))

A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

kratnie_k = []
for i in range(n):
    for j in range(n):
        if A[i][j] % k == 0:
            kratnie_k.append(A[i][j])

if len(kratnie_k) != 0:
    count = len(kratnie_k)
    max_element = max(kratnie_k)
    print('Количество элементов, кратных', k, ':', count)
    print('Наибольший:', max_element)
else:
    print('Нет элементов, кратных', k)

# 2. В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.
n = int(input('Введите размер матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

max_abs = abs(A[0][0])
imax, jmax = 0, 0
for i in range(n):
    for j in range(n):
        if abs(A[i][j]) > max_abs:
            max_abs = abs(A[i][j])
            imax, jmax = i, j

# Новая матрица без строки imax и столбца jmax
B = []
for i in range(n):
    if i == imax:
        continue
    row = []
    for j in range(n):
        if j == jmax:
            continue
        row.append(A[i][j])
    B.append(row)

for i in range(n - 1):
    for j in range(n - 1):
        print(B[i][j], end=' ')
    print()

# Вариант 10.
# 1. Найти максимальный среди всех элементов тех строк заданной
# матрицы, которые упорядочены (либо по возрастанию, либо по
# убыванию).
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

A = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

def is_sorted(row):
    asc = all(row[i] <= row[i+1] for i in range(len(row)-1))
    desc = all(row[i] >= row[i+1] for i in range(len(row)-1))
    return asc or desc

max_sorted = None
for row in A:
    if is_sorted(row):
        current_max = max(row)
        if max_sorted is None or current_max > max_sorted:
            max_sorted = current_max

if max_sorted is not None:
    print('Максимальный элемент среди упорядоченных строк:', max_sorted)
else:
    print('Нет упорядоченных строк')

# 2. Расположить столбцы матрицы D[M, N] в порядке возрастания
# элементов k-й строки (1 <= k <= М).
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))
k = int(input('Введите номер строки для сортировки (от 0 до ' + str(M - 1) + '): '))

D = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    D.append(b)

sorted_indexes = sorted(range(N), key=lambda j: D[k][j])

new_D = []
for i in range(M):
    new_row = [D[i][id] for id in sorted_indexes]
    new_D.append(new_row)

for i in range(M):
    for j in range(N):
        print(new_D[i][j], end=' ')
    print()

# Вариант 11.
# 1. В данной действительной квадратной матрице порядка п найти
# сумму элементов строки, в которой расположен элемент с наименьшим
# значением. Предполагается, что такой элемент единственный.
n = int(input('Введите ширину матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

min_val = A[0][0]
min_i, min_j = 0, 0
for i in range(n):
    for j in range(n):
        if A[i][j] < min_val:
            min_val = A[i][j]
            min_i = i

# Сумма строки, где находится минимальный элемент
abs_row_sum = sum(A[min_i])

print('Сумма элементов строки с наименьшим элементом:', abs_row_sum)

# 2. Среди столбцов заданной целочисленной матрицы, содержащих
# только такие элементы, которые по модулю не больше 10, найти столбец
# с минимальным произведением элементов и поменять местами с
# соседним.
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

correct_columns = []
for j in range(N):
    if all(abs(A[i][j]) <= 10 for i in range(M)):
        prod = 1
        for i in range(M):
            prod *= A[i][j]
        correct_columns.append((prod, j))

if len(correct_columns) == 0:
    print("Нет столбцов, удовлетворяющих условию.")
else:
    # Столбец с минимальным произведением
    min_prod, min_col_id = min(correct_columns, key=lambda x: x[0])

    # Меняем местами с соседним столбцом
    swap_column = None
    if min_col_id + 1 < N:  # Правый
        swap_column = min_col_id + 1
    elif min_col_id - 1 >= 0:  # Левый
        swap_column = min_col_id - 1
    else:
        print("Невозможно поменять местами — только один столбец")
        swap_column = None

    if swap_column is not None:
        # Меняем столбцы местами
        for i in range(M):
            A[i][min_col_id], A[i][swap_column] = A[i][swap_column], A[i][min_col_id]

    for i in range(M):
        for j in range(N):
            print(A[i][j], end=' ')
        print()

# Вариант 12.
# 1. Для заданной квадратной матрицы найти такие k, что k-я строка
# матрицы совпадает с k-м столбцом.
n = int(input('Введите размер матрицы: '))
A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

result = []
for k in range(n):
    row_k = A[k]
    col_k = [A[i][k] for i in range(n)]
    if row_k == col_k:
        result.append(k)

print('Индексы строк, совпадающих с соответствующими столбцами:', result)

# 2. Дана действительная матрица размером n х m. Требуется
# преобразовать матрицу: поэлементно вычесть последнюю строку из всех
# строк, кроме последней.
n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))

A = []
for i in range(n):
    b = []
    for j in range(m):
        print('Введите [', i, ',', j, '] элемент')
        b.append(float(input()))
    A.append(b)

last_row = A[n - 1]

# Вычитаем последнюю строку из всех, кроме последней
for i in range(n - 1):
    for j in range(m):
        A[i][j] -= last_row[j]

for i in range(n):
    for j in range(m):
        print(A[i][j], end=' ')
    print()

# Вариант 13.
# 1. Определить наименьший элемент каждой четной строки матрицы
# А[М, N].
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

for i in range(0, M, 2):  # только чётные строки
    min_in_row = min(A[i])
    print('Минимальный элемент в строке', i, '=', min_in_row)

# 2. Найти наибольший и наименьший элементы прямоугольной
# матрицы и поменять их местами.
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

min_val = A[0][0]
max_val = A[0][0]
min_i, min_j = 0, 0
max_i, max_j = 0, 0

for i in range(M):
    for j in range(N):
        if A[i][j] < min_val:
            min_val = A[i][j]
            min_i, min_j = i, j
        if A[i][j] > max_val:
            max_val = A[i][j]
            max_i, max_j = i, j

# Меняем местами
A[min_i][min_j], A[max_i][max_j] = A[max_i][max_j], A[min_i][min_j]

# Вывод
for i in range(M):
    for j in range(N):
        print(A[i][j], end=' ')
    print()

# Вариант 14.
# 1. Задана квадратная матрица. Переставить строку с максимальным
# элементом на главной диагонали со строкой с заданным номером m.
n = int(input('Введите размер матрицы: '))
m = int(input('Введите номер строки m (от 0 до ' + str(n - 1) + '): '))

A = []
for i in range(n):
    b = []
    for j in range(n):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

# Максимальный элемент на главной диагонали и его строка
max_diag = A[0][0]
imax = 0
for i in range(n):
    if A[i][i] > max_diag:
        max_diag = A[i][i]
        imax = i

A[imax], A[m] = A[m], A[imax]

for i in range(n):
    for j in range(n):
        print(A[i][j], end=' ')
    print()

# 2. Составить программу, которая заполняет квадратную матрицу
# порядка п натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по
# спирали».
# Например, для п = 5 получаем следующую матрицу:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 14 12 11 10 9
n = int(input('Введите размер матрицы: '))

matrix = [[0] * n for _ in range(n)]

num = 1  # текущее число для заполнения
top, bottom = 0, n - 1
left, right = 0, n - 1

while top <= bottom and left <= right:
    # Слева направо (верхняя строка)
    for j in range(left, right + 1):
        matrix[top][j] = num
        num += 1
    top += 1

    # Сверху вниз (правый столбец)
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1

    # Справа налево (нижняя строка)
    if top <= bottom:
        for j in range(right, left - 1, -1):
            matrix[bottom][j] = num
            num += 1
        bottom -= 1

    # Снизу вверх (левый столбец)
    if left <= right:
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

# Вариант 15.
# 1. Определить номера строк матрицы R[M, N], хотя бы один элемент
# которых равен с, и элементы этих строк умножить на d.
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))
c = int(input('Введите значение c: '))
d = int(input('Введите значение d: '))

R = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    R.append(b)

for i in range(M):
    if c in R[i]:  # проверяем, есть ли c в строке
        for j in range(N):
            R[i][j] *= d  # умножаем всю строку на d

# Вывод
for i in range(M):
    for j in range(N):
        print(R[i][j], end=' ')
    print()

# 2. Среди тех строк целочисленной матрицы, которые содержат только
# нечетные элементы, найти строку с максимальной суммой модулей
# элементов.
M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = []
for i in range(M):
    b = []
    for j in range(N):
        print('Введите [', i, ',', j, '] элемент')
        b.append(int(input()))
    A.append(b)

correct_rows = []
for i in range(M):
    if all(x % 2 != 0 for x in A[i]):  # проверяем, все ли нечётные
        abs_row_sum = sum(abs(x) for x in A[i])
        correct_rows.append((abs_row_sum, A[i]))

if correct_rows:
    max_row = max(correct_rows, key=lambda x: x[0])[1]
    print('Строка с максимальной суммой модулей среди строк с нечётными элементами:')
    for x in max_row:
        print(x, end=' ')
    print()
else:
    print('Нет строк, содержащих только нечётные элементы.')
