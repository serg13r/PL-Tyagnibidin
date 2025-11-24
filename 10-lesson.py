# Вариант 1.
# 1. Вычислить сумму и число положительных элементов матрицы A[N,
# N], находящихся над главной диагональю.
with open('variant_1_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

f = []
for i in range(n):
    for j in range(n):
        if i < j:
            if A[i][j] > 0:
                f.append(A[i][j])

with open('variant_1_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Сумма положит элементов {sum(f)} Кол положит элементов {len(f)}')

# 2. Дана матрица B[N, М]. Найти в каждой строке матрицы
# максимальный и минимальный элементы и поменять их с первым и
# последним элементами строки соответственно.
with open('variant_1_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_1_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 2.
# 1. Дана целая квадратная матрица n-го порядка. Определить,
# является ли она магическим квадратом, т. е. такой матрицей, в которой
# суммы элементов во всех строках и столбцах одинаковы.
with open('variant_2_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

etalon_summi = sum(A[0])
magic = all(sum(row) == etalon_summi for row in A) and \
        all(sum(A[i][j] for i in range(n)) == etalon_summi for j in range(n)) and \
        sum(A[i][i] for i in range(n)) == etalon_summi and \
        sum(A[i][n-1-i] for i in range(n)) == etalon_summi

with open('variant_2_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write('Является' if magic else 'Не является')

# 2. Дана прямоугольная матрица A[N, N]. Переставить первый и
# последний столбцы местами и вывести на экран.
with open('variant_2_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

for i in range(n):
    A[i][0], A[i][n - 1] = A[i][n - 1], A[i][0]

with open('variant_2_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 3.
# 1. Определить, является ли заданная целая квадратная матрица n-го
# порядка симметричной (относительно главной диагонали).
with open('variant_3_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

symmetric = all(A[i][j] == A[j][i] for i in range(n) for j in range(i + 1, n))

with open('variant_3_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write('Симметрична' if symmetric else 'Не симметрична')

# 2. Дана вещественная матрица размером n х m. Переставляя ее
# строки и столбцы, добиться того, чтобы наибольший элемент (или один
# из них) оказался в верхнем левом углу.
with open('variant_3_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_3_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 4.
# 1. Дана прямоугольная матрица. Найти строку с наибольшей и строку
# с наименьшей суммой элементов. Вывести на печать найденные строки и
# суммы их элементов.
with open('variant_4_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_4_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Минимальная строка: {B[min_idx]} Сумма: {prevmin}\n')
    out.write(f'Максимальная строка: {B[max_idx]} Сумма: {prevmax}')

# 2. Дана квадратная матрица A[N, N], Записать на место
# отрицательных элементов матрицы нули, а на место положительных —
# единицы.
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде.
with open('variant_4_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            A[i][j] = 1 # на место положительных единицы.
        elif A[i][j] < 0:
            A[i][j] = 0 # на место отрицательных нули.

with open('variant_4_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            if j <= i:  # Выводим только элементы на и ниже диагонали, треугольник
                out.write(f'{A[i][j]} ')
            else:
                out.write('  ')
        out.write('\n')

# Вариант 5.
# 1. Упорядочить по возрастанию элементы каждой строки матрицы
# размером n х m.
with open('variant_5_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

for i in range(n):
    B[i].sort()  # Сортировка по возрастанию

with open('variant_5_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# 2. Дана действительная матрица размером n х m, все элементы
# которой различны. В каждой строке выбирается элемент с наименьшим
# значением. Если число четное, то заменяется нулем, нечетное -
# единицей. Вывести на экран новую матрицу.
with open('variant_5_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(float, lines[i + 2].split()))
    B.append(row)

for i in range(n):
    minimum = min(B[i])
    minindex = B[i].index(minimum)
    B[i][minindex] = 1 if (minimum % 2 != 0) else 0

with open('variant_5_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 6.
# 1. Дана целочисленная квадратная матрица. Найти в каждой строке
# наибольший элемент и в каждом столбце наименьший. Вывести на
# экран.
with open('variant_6_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

with open('variant_6_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        out.write(f'Наибольший элемент строки {i} = {max(A[i])}\n')
    for i in range(n):
        col = [A[j][i] for j in range(n)]
        out.write(f'Наименьший элемент столбца {i} = {min(col)}\n')

# 2. Дана действительная квадратная матрица порядка N (N —
# нечетное), все элементы которой различны. Найти наибольший элемент
# среди стоящих на главной и побочной диагоналях и поменять его
# местами с элементом, стоящим на пересечении этих диагоналей.
with open('variant_6_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

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

with open('variant_6_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 7.
# 1. Квадратная матрица, симметричная относительно главной
# диагонали, задана верхним треугольником в виде одномерного массива.
# Восстановить исходную матрицу и напечатать по строкам.
with open('variant_7_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
treugoln = list(map(int, lines[1].split()))

A = [[0] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(i, n):
        A[i][j] = treugoln[k]
        A[j][i] = treugoln[k]  # симметричный элемент
        k += 1

with open('variant_7_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# 2. Для заданной квадратной матрицы сформировать одномерный
# массив из ее диагональных элементов. Найти след матрицы,
# просуммировав элементы одномерного массива. Преобразовать
# исходную матрицу по правилу: четные строки разделить на полученное
# значение, нечетные оставить без изменения.
with open('variant_7_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

diagonal = [A[i][i] for i in range(n)]

sum_diag = sum(diagonal)

for i in range(n):
    if i % 2 == 0:  # чётная строка
        for j in range(n):
            A[i][j] /= sum_diag

with open('variant_7_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 8.
# 1. Задана матрица порядка n и число к. Разделить элементы k-й
# строки на диагональный элемент, расположенный в этой строке.
with open('variant_8_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
k = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(float, lines[i + 2].split()))
    A.append(row)

diag_element = A[k][k]

for j in range(n):
    A[k][j] /= diag_element

with open('variant_8_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# 2. Задана квадратная матрица. Получить транспонированную
# матрицу (перевернутую относительно главной диагонали) и вывести на
# экран.
with open('variant_8_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

with open('variant_8_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[j][i]} ')  # i и j поменяли местами
        out.write('\n')

# Вариант 9.
# 1. Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
with open('variant_9_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
k = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

kratnie_k = []
for i in range(n):
    for j in range(n):
        if A[i][j] % k == 0:
            kratnie_k.append(A[i][j])

with open('variant_9_1_vivod.txt', 'w', encoding='utf-8') as out:
    if len(kratnie_k) != 0:
        count = len(kratnie_k)
        max_element = max(kratnie_k)
        out.write(f'Количество элементов, кратных {k}: {count}\n')
        out.write(f'Наибольший: {max_element}')
    else:
        out.write(f'Нет элементов, кратных {k}')

# 2. В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.
with open('variant_9_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

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

with open('variant_9_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n - 1):
        for j in range(n - 1):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 10.
# 1. Найти максимальный среди всех элементов тех строк заданной
# матрицы, которые упорядочены (либо по возрастанию, либо по
# убыванию).
with open('variant_10_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

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

with open('variant_10_1_vivod.txt', 'w', encoding='utf-8') as out:
    if max_sorted is not None:
        out.write(f'Максимальный элемент среди упорядоченных строк: {max_sorted}')
    else:
        out.write('Нет упорядоченных строк')

# 2. Расположить столбцы матрицы D[M, N] в порядке возрастания
# элементов k-й строки (1 <= k <= М).
with open('variant_10_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())
k = int(lines[2].strip())

D = []
for i in range(M):
    row = list(map(int, lines[i + 3].split()))
    D.append(row)

sorted_indexes = sorted(range(N), key=lambda j: D[k][j])

new_D = []
for i in range(M):
    new_row = [D[i][id] for id in sorted_indexes]
    new_D.append(new_row)

with open('variant_10_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(M):
        for j in range(N):
            out.write(f'{new_D[i][j]} ')
        out.write('\n')

# Вариант 11.
# 1. В данной действительной квадратной матрице порядка п найти
# сумму элементов строки, в которой расположен элемент с наименьшим
# значением. Предполагается, что такой элемент единственный.
with open('variant_11_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

min_val = A[0][0]
min_i, min_j = 0, 0
for i in range(n):
    for j in range(n):
        if A[i][j] < min_val:
            min_val = A[i][j]
            min_i = i

# Сумма строки, где находится минимальный элемент
abs_row_sum = sum(A[min_i])

with open('variant_11_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Сумма элементов строки с наименьшим элементом: {abs_row_sum}')

# 2. Среди столбцов заданной целочисленной матрицы, содержащих
# только такие элементы, которые по модулю не больше 10, найти столбец
# с минимальным произведением элементов и поменять местами с
# соседним.
with open('variant_11_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())

A = []
for i in range(M):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

correct_columns = []
for j in range(N):
    if all(abs(A[i][j]) <= 10 for i in range(M)):
        prod = 1
        for i in range(M):
            prod *= A[i][j]
        correct_columns.append((prod, j))

with open('variant_11_2_vivod.txt', 'w', encoding='utf-8') as out:
    if len(correct_columns) == 0:
        out.write("Нет столбцов, удовлетворяющих условию.")
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
            out.write("Невозможно поменять местами — только один столбец\n")
            swap_column = None

        if swap_column is not None:
            # Меняем столбцы местами
            for i in range(M):
                A[i][min_col_id], A[i][swap_column] = A[i][swap_column], A[i][min_col_id]

        for i in range(M):
            for j in range(N):
                out.write(f'{A[i][j]} ')
            out.write('\n')

# Вариант 1.
# 1. Вычислить сумму и число положительных элементов матрицы A[N,
# N], находящихся над главной диагональю.
with open('variant_1_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

f = []
for i in range(n):
    for j in range(n):
        if i < j:
            if A[i][j] > 0:
                f.append(A[i][j])

with open('variant_1_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Сумма положит элементов {sum(f)} Кол положит элементов {len(f)}')

# 2. Дана матрица B[N, М]. Найти в каждой строке матрицы
# максимальный и минимальный элементы и поменять их с первым и
# последним элементами строки соответственно.
with open('variant_1_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_1_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 2.
# 1. Дана целая квадратная матрица n-го порядка. Определить,
# является ли она магическим квадратом, т. е. такой матрицей, в которой
# суммы элементов во всех строках и столбцах одинаковы.
with open('variant_2_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

etalon_summi = sum(A[0])
magic = all(sum(row) == etalon_summi for row in A) and \
        all(sum(A[i][j] for i in range(n)) == etalon_summi for j in range(n)) and \
        sum(A[i][i] for i in range(n)) == etalon_summi and \
        sum(A[i][n-1-i] for i in range(n)) == etalon_summi

with open('variant_2_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write('Является' if magic else 'Не является')

# 2. Дана прямоугольная матрица A[N, N]. Переставить первый и
# последний столбцы местами и вывести на экран.
with open('variant_2_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

for i in range(n):
    A[i][0], A[i][n - 1] = A[i][n - 1], A[i][0]

with open('variant_2_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 3.
# 1. Определить, является ли заданная целая квадратная матрица n-го
# порядка симметричной (относительно главной диагонали).
with open('variant_3_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

symmetric = all(A[i][j] == A[j][i] for i in range(n) for j in range(i + 1, n))

with open('variant_3_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write('Симметрична' if symmetric else 'Не симметрична')

# 2. Дана вещественная матрица размером n х m. Переставляя ее
# строки и столбцы, добиться того, чтобы наибольший элемент (или один
# из них) оказался в верхнем левом углу.
with open('variant_3_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_3_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 4.
# 1. Дана прямоугольная матрица. Найти строку с наибольшей и строку
# с наименьшей суммой элементов. Вывести на печать найденные строки и
# суммы их элементов.
with open('variant_4_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

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

with open('variant_4_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Минимальная строка: {B[min_idx]} Сумма: {prevmin}\n')
    out.write(f'Максимальная строка: {B[max_idx]} Сумма: {prevmax}')

# 2. Дана квадратная матрица A[N, N], Записать на место
# отрицательных элементов матрицы нули, а на место положительных —
# единицы.
# Вывести на печать нижнюю треугольную матрицу в общепринятом виде.
with open('variant_4_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

for i in range(n):
    for j in range(n):
        if A[i][j] > 0:
            A[i][j] = 1 # на место положительных единицы.
        elif A[i][j] < 0:
            A[i][j] = 0 # на место отрицательных нули.

with open('variant_4_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            if j <= i:  # Выводим только элементы на и ниже диагонали, треугольник
                out.write(f'{A[i][j]} ')
            else:
                out.write('  ')
        out.write('\n')

# Вариант 5.
# 1. Упорядочить по возрастанию элементы каждой строки матрицы
# размером n х m.
with open('variant_5_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    B.append(row)

for i in range(n):
    B[i].sort()  # Сортировка по возрастанию

with open('variant_5_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# 2. Дана действительная матрица размером n х m, все элементы
# которой различны. В каждой строке выбирается элемент с наименьшим
# значением. Если число четное, то заменяется нулем, нечетное -
# единицей. Вывести на экран новую матрицу.
with open('variant_5_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

B = []
for i in range(n):
    row = list(map(float, lines[i + 2].split()))
    B.append(row)

for i in range(n):
    minimum = min(B[i])
    minindex = B[i].index(minimum)
    B[i][minindex] = 1 if (minimum % 2 != 0) else 0

with open('variant_5_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 6.
# 1. Дана целочисленная квадратная матрица. Найти в каждой строке
# наибольший элемент и в каждом столбце наименьший. Вывести на
# экран.
with open('variant_6_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

with open('variant_6_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        out.write(f'Наибольший элемент строки {i} = {max(A[i])}\n')
    for i in range(n):
        col = [A[j][i] for j in range(n)]
        out.write(f'Наименьший элемент столбца {i} = {min(col)}\n')

# 2. Дана действительная квадратная матрица порядка N (N —
# нечетное), все элементы которой различны. Найти наибольший элемент
# среди стоящих на главной и побочной диагоналях и поменять его
# местами с элементом, стоящим на пересечении этих диагоналей.
with open('variant_6_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

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

with open('variant_6_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 7.
# 1. Квадратная матрица, симметричная относительно главной
# диагонали, задана верхним треугольником в виде одномерного массива.
# Восстановить исходную матрицу и напечатать по строкам.
with open('variant_7_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
treugoln = list(map(int, lines[1].split()))

A = [[0] * n for _ in range(n)]

k = 0
for i in range(n):
    for j in range(i, n):
        A[i][j] = treugoln[k]
        A[j][i] = treugoln[k]  # симметричный элемент
        k += 1

with open('variant_7_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# 2. Для заданной квадратной матрицы сформировать одномерный
# массив из ее диагональных элементов. Найти след матрицы,
# просуммировав элементы одномерного массива. Преобразовать
# исходную матрицу по правилу: четные строки разделить на полученное
# значение, нечетные оставить без изменения.
with open('variant_7_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

diagonal = [A[i][i] for i in range(n)]

sum_diag = sum(diagonal)

for i in range(n):
    if i % 2 == 0:  # чётная строка
        for j in range(n):
            A[i][j] /= sum_diag

with open('variant_7_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 8.
# 1. Задана матрица порядка n и число к. Разделить элементы k-й
# строки на диагональный элемент, расположенный в этой строке.
with open('variant_8_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
k = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(float, lines[i + 2].split()))
    A.append(row)

diag_element = A[k][k]

for j in range(n):
    A[k][j] /= diag_element

with open('variant_8_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# 2. Задана квадратная матрица. Получить транспонированную
# матрицу (перевернутую относительно главной диагонали) и вывести на
# экран.
with open('variant_8_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

with open('variant_8_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[j][i]} ')  # i и j поменяли местами
        out.write('\n')

# Вариант 9.
# 1. Для целочисленной квадратной матрицы найти число элементов,
# кратных k, и наибольший из этих элементов.
with open('variant_9_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
k = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

kratnie_k = []
for i in range(n):
    for j in range(n):
        if A[i][j] % k == 0:
            kratnie_k.append(A[i][j])

with open('variant_9_1_vivod.txt', 'w', encoding='utf-8') as out:
    if len(kratnie_k) != 0:
        count = len(kratnie_k)
        max_element = max(kratnie_k)
        out.write(f'Количество элементов, кратных {k}: {count}\n')
        out.write(f'Наибольший: {max_element}')
    else:
        out.write(f'Нет элементов, кратных {k}')

# 2. В данной действительной квадратной матрице порядка n найти
# наибольший по модулю элемент. Получить квадратную матрицу порядка
# n — 1 путем отбрасывания из исходной матрицы строки и столбца, на
# пересечении которых расположен элемент с найденным значением.
with open('variant_9_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

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

with open('variant_9_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n - 1):
        for j in range(n - 1):
            out.write(f'{B[i][j]} ')
        out.write('\n')

# Вариант 10.
# 1. Найти максимальный среди всех элементов тех строк заданной
# матрицы, которые упорядочены (либо по возрастанию, либо по
# убыванию).
with open('variant_10_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

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

with open('variant_10_1_vivod.txt', 'w', encoding='utf-8') as out:
    if max_sorted is not None:
        out.write(f'Максимальный элемент среди упорядоченных строк: {max_sorted}')
    else:
        out.write('Нет упорядоченных строк')

# 2. Расположить столбцы матрицы D[M, N] в порядке возрастания
# элементов k-й строки (1 <= k <= М).
with open('variant_10_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())
k = int(lines[2].strip())

D = []
for i in range(M):
    row = list(map(int, lines[i + 3].split()))
    D.append(row)

sorted_indexes = sorted(range(N), key=lambda j: D[k][j])

new_D = []
for i in range(M):
    new_row = [D[i][id] for id in sorted_indexes]
    new_D.append(new_row)

with open('variant_10_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(M):
        for j in range(N):
            out.write(f'{new_D[i][j]} ')
        out.write('\n')

# Вариант 11.
# 1. В данной действительной квадратной матрице порядка п найти
# сумму элементов строки, в которой расположен элемент с наименьшим
# значением. Предполагается, что такой элемент единственный.
with open('variant_11_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(float, lines[i + 1].split()))
    A.append(row)

min_val = A[0][0]
min_i, min_j = 0, 0
for i in range(n):
    for j in range(n):
        if A[i][j] < min_val:
            min_val = A[i][j]
            min_i = i

# Сумма строки, где находится минимальный элемент
abs_row_sum = sum(A[min_i])

with open('variant_11_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Сумма элементов строки с наименьшим элементом: {abs_row_sum}')

# 2. Среди столбцов заданной целочисленной матрицы, содержащих
# только такие элементы, которые по модулю не больше 10, найти столбец
# с минимальным произведением элементов и поменять местами с
# соседним.
with open('variant_11_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())

A = []
for i in range(M):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

correct_columns = []
for j in range(N):
    if all(abs(A[i][j]) <= 10 for i in range(M)):
        prod = 1
        for i in range(M):
            prod *= A[i][j]
        correct_columns.append((prod, j))

with open('variant_11_2_vivod.txt', 'w', encoding='utf-8') as out:
    if len(correct_columns) == 0:
        out.write("Нет столбцов, удовлетворяющих условию.")
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
            out.write("Невозможно поменять местами — только один столбец\n")
            swap_column = None

        if swap_column is not None:
            # Меняем столбцы местами
            for i in range(M):
                A[i][min_col_id], A[i][swap_column] = A[i][swap_column], A[i][min_col_id]

        for i in range(M):
            for j in range(N):
                out.write(f'{A[i][j]} ')
            out.write('\n')

# Вариант 12.
# 1. Для заданной квадратной матрицы найти такие k, что k-я строка
# матрицы совпадает с k-м столбцом.
with open('variant_12_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
A = []
for i in range(n):
    row = list(map(int, lines[i + 1].split()))
    A.append(row)

result = []
for k in range(n):
    row_k = A[k]
    col_k = [A[i][k] for i in range(n)]
    if row_k == col_k:
        result.append(k)

with open('variant_12_1_vivod.txt', 'w', encoding='utf-8') as out:
    out.write(f'Индексы строк, совпадающих с соответствующими столбцами: {result}')

# 2. Дана действительная матрица размером n х m. Требуется
# преобразовать матрицу: поэлементно вычесть последнюю строку из всех
# строк, кроме последней.
with open('variant_12_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(float, lines[i + 2].split()))
    A.append(row)

last_row = A[n - 1]

# Вычитаем последнюю строку из всех, кроме последней
for i in range(n - 1):
    for j in range(m):
        A[i][j] -= last_row[j]

with open('variant_12_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(m):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 13.
# 1. Определить наименьший элемент каждой четной строки матрицы
# А[М, N].
with open('variant_13_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())

A = []
for i in range(M):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

with open('variant_13_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(0, M, 2):  # только чётные строки
        min_in_row = min(A[i])
        out.write(f'Минимальный элемент в строке {i} = {min_in_row}\n')

# 2. Найти наибольший и наименьший элементы прямоугольной
# матрицы и поменять их местами.
with open('variant_13_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())

A = []
for i in range(M):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

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

with open('variant_13_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(M):
        for j in range(N):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# Вариант 14.
# 1. Задана квадратная матрица. Переставить строку с максимальным
# элементом на главной диагонали со строкой с заданным номером m.
with open('variant_14_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

n = int(lines[0].strip())
m = int(lines[1].strip())

A = []
for i in range(n):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

# Максимальный элемент на главной диагонали и его строка
max_diag = A[0][0]
imax = 0
for i in range(n):
    if A[i][i] > max_diag:
        max_diag = A[i][i]
        imax = i

A[imax], A[m] = A[m], A[imax]

with open('variant_14_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{A[i][j]} ')
        out.write('\n')

# 2. Составить программу, которая заполняет квадратную матрицу
# порядка п натуральными числами 1, 2, 3, ..., n2, записывая их в нее «по
# спирали».
with open('variant_14_2_vvod.txt', 'r', encoding='utf-8') as f:
    n = int(f.readline().strip())

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

with open('variant_14_2_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(n):
        for j in range(n):
            out.write(f'{matrix[i][j]} ')
        out.write('\n')

# Вариант 15.
# 1. Определить номера строк матрицы R[M, N], хотя бы один элемент
# которых равен с, и элементы этих строк умножить на d.
with open('variant_15_1_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())
c = int(lines[2].strip())
d = int(lines[3].strip())

R = []
for i in range(M):
    row = list(map(int, lines[i + 4].split()))
    R.append(row)

for i in range(M):
    if c in R[i]:  # проверяем, есть ли c в строке
        for j in range(N):
            R[i][j] *= d  # умножаем всю строку на d

with open('variant_15_1_vivod.txt', 'w', encoding='utf-8') as out:
    for i in range(M):
        for j in range(N):
            out.write(f'{R[i][j]} ')
        out.write('\n')

# 2. Среди тех строк целочисленной матрицы, которые содержат только
# нечетные элементы, найти строку с максимальной суммой модулей
# элементов.
with open('variant_15_2_vvod.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

M = int(lines[0].strip())
N = int(lines[1].strip())

A = []
for i in range(M):
    row = list(map(int, lines[i + 2].split()))
    A.append(row)

correct_rows = []
for i in range(M):
    if all(x % 2 != 0 for x in A[i]):  # проверяем, все ли нечётные
        abs_row_sum = sum(abs(x) for x in A[i])
        correct_rows.append((abs_row_sum, A[i]))

with open('variant_15_2_vivod.txt', 'w', encoding='utf-8') as out:
    if correct_rows:
        max_row = max(correct_rows, key=lambda x: x[0])[1]
        out.write('Строка с максимальной суммой модулей среди строк с нечётными элементами:\n')
        for x in max_row:
            out.write(f'{x} ')
        out.write('\n')
    else:
        out.write('Нет строк, содержащих только нечётные элементы.')