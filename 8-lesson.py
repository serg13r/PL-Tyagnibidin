from math import *
from random import randint
# Вариант 1.
# 1. Составить программу для вычисления площади разных геометрических
# фигур.
def figure_area_counter(mode, values):
    if mode == 0 and len(values) == 2: # Прямоугольник, квадрат
        return values[0] * values[1]
    elif len(values) == 3: # Треугольник
        p = (values[0] + values[1] + values[2]) / 2
        return sqrt(p * (p-values[0]) * (p-values[1]) * (p-values[2]))
    return 0

if int(input('Находим площадь:\n0 - Прямоугольник, квадрат\n1 - Треугольник\n')) == 0:
    print('Площадь =',figure_area_counter(0, [int(input('Введите размер фигуры ')) for _ in range(2)]))
else:
    print('Площадь =',figure_area_counter(1, [int(input('Введите размер фигуры ')) for _ in range(3)]))

# 2. Даны 3 различных массива целых чисел (размер каждого не превышает
# 15). В каждом массиве найти сумму элементов и среднеарифметическое
# значение.
def average(values):
    return sum(values) / len(values)

for i in range(1,4):
    print('Массив',i)
    arr = [randint(0, 100) for _ in range(randint(1, 15))]
    print('Сумма', sum(arr))
    print('Среднее арифметическое', average(arr))

# Вариант 2.
# 1. Вычислить площадь правильного шестиугольника со стороной а,
# используя подпрограмму вычисления площади треугольника.
def triangle_area(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))

def equal_hexagon_area(a):
    # Правильный шестиугольник = 6 равносторонних треугольников со стороной a
    return 6 * triangle_area(a, a, a)

a = float(input("Введите сторону шестиугольника: "))
print("Площадь шестиугольника:", equal_hexagon_area(a))

# 2. Пользователь вводит две стороны трех прямоугольников. Вывести их
# площади.
def rectangle_area(values):
    if len(values) == 2:
        return values[0] * values[1]
    return 0

for i in range(1,4):
    print('Прямоугольник',i)
    print('Площадь =', rectangle_area([int(input('Введите размер стороны ')) for _ in range(2)]))

# Вариант 3.
# 1. Даны катеты двух прямоугольных треугольников. Написать функцию
# вычисления длины гипотенузы этих треугольников. Сравнить и вывести какая из
# гипотенуз больше, а какая меньше.
def hypotenuse(values):
    if len(values) == 2:
        return sqrt(values[0] ** 2 + values[1] ** 2)
    return 0

hh = []
for i in range(1,3):
    print('Прямоугольный треугольник',i)
    area = hypotenuse([int(input('Введите размер катета ')) for _ in range(2)])
    print('Гипотенуза =', area)
    hh.append(area)

h1, h2 = hh
if h1 > h2:
    print('Гипотенуза треугольника 1 больше гипотенузы треугольника 2')
elif h1 < h2:
    print('Гипотенуза треугольника 1 меньше гипотенузы треугольника 2')
else:
    print('Гипотенузы треугольников равны')


# 2. Преобразовать строку так, чтобы буквы каждого слова в ней были
# отсортированы по алфавиту.
def sort_letters_in_words(s):
    sorted_words = [''.join(sorted(word)) for word in s.split()]
    return ' '.join(sorted_words)
sortedlists = input('Введите строку для преобразования ')
print('Отсортированная строка:', sort_letters_in_words(sortedlists))

# Вариант 4.
# 1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить
# программу деления дроби на дробь. Ответ должен быть несократимой дробью.
# Использовать подпрограмму алгоритма Евклида для определения НОД.
def nodEvklida(a, b):
    while b != 0:
        a, b = b, a % b
    return a

A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))
num = A * D # числитель
den = B * C # знаменатель

g = nodEvklida(num, den)
num //= g
den //= g
print('Результат:', num, '/', den)

# 2. Задана окружность (x-a)2 + (y-b)2 = R2 и точки Р(р1, р2), F(f1, f1), L(l1,l2).
# Выяснить и вывести на экран, сколько точек лежит внутри окружности.
# Проверку, лежит ли точка внутри окружности, оформить в виде процедуры.
def is_inside(x, y, a, b, r):
    return (x - a) ** 2 + (y - b) ** 2 < r ** 2

a, b, R = map(int, input("Введите a, b, R через пробел: ").split())
points = []
for name in ['P', 'F', 'L']:
    coords = [int(input(f'Введите координаты точки {name}{i} ')) for i in range(2)]
    points.append(coords)

count = sum(1 for x, y in points if is_inside(x, y, a, b, R))
print("Количество точек внутри окружности:", count)

# Вариант 5.
# 1. Даны две дроби A/B и C/D (А, В, С, D — натуральные числа). Составить
# программу вычитания из первой дроби второй. Ответ должен быть
# несократимой дробью. Использовать подпрограмму алгоритма Евклида для
# определения НОД.
A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
D = int(input("D = "))

# Вычитание дробей
num = A * D - C * B  # числитель результата
den = B * D  # знаменатель результата

if den == 0:
    print("Знаменатель равен нулю")
else:
    g = nodEvklida(abs(num), den) # тут формула Евклида
    num //= g
    den //= g

    if den == 1:
        print("Результат:", num)
    else:
        print("Результат:", f"{num}/{den}")

# 2. Напишите программу, которая выводит в одну строчку все делители
# переданного ей числа, разделяя их пробелами.
def dividers(n):
    if n == 1:
        return [1]
    divs = {1, n}  # Начинаем с 1 и самого числа
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)
    return sorted(divs)

n = int(input('Введите число: '))
print(' '.join(map(str, dividers(n))))

# Вариант 6.
# 1. Составить программу нахождения наибольшего общего делителя (НОД) и
# наименьшего общего кратного (НОК) двух натуральных чисел НОК(А, В) =
# (A*B)/НОД(A,B). Использовать подпрограмму алгоритма Евклида для
# определения НОД.
def nok(a, b):
    n = nodEvklida(a, b)
    return (a * b) // n

print(nok(int(input('Введите первое число')),
            int(input('Введите второе число'))))

# 2. Cоставить программу вычисления площади выпуклого четырехугольника,
# заданного длинами четырех сторон и диагонали.
def quadrilateral_area(a, b, c, d, e):
    # Разбиваем четырёхугольник диагональю 'e' на два треугольника:
    return triangle_area(a, b, e) + triangle_area(c, d, e)

a = int(input("Введите длину стороны a: "))
b = int(input("Введите длину стороны b: "))
c = int(input("Введите длину стороны c: "))
d = int(input("Введите длину стороны d: "))
e = int(input("Введите длину диагонали e: "))
print('Площадь четырёхугольника:', quadrilateral_area(a, b, c, d, e))

# Вариант 7.
# 1. Даны числа X, Y, Z, Т — длины сторон четырехугольника. Вычислить его
# площадь, если угол между сторонами длиной X и У — прямой. Использовать
# две подпрограммы для вычисления площадей: прямоугольного треугольника и
# прямоугольника.
def rectangle_area(a, b):
  return a * b

def right_triangle_area(a, b):
  return 0.5 * a * b

x = int(input("Введите длину стороны (высота) X: "))
y = int(input("Введите длину стороны (большее основание) Y: "))
z = int(input("Введите длину стороны (боковая сторона) Z: "))
t = int(input("Введите длину стороны (меньшее основание) T: "))

area_rect = rectangle_area(x, t) # Площадь прямоугольной части
area_tri = right_triangle_area(x, y - t) # Площадь треугольной части (разница оснований y-t)
print('Площадь четырёхугольника:', area_rect + area_tri)

# 2. Напишите программу, которая переводит переданное ей
# неотрицательное целое число в 10-значный восьмеричный код, сохранив
# лидирующие нули.
def to_octal(num):
    octal_str = f"{num:o}" # число в восьмеричную строку
    return octal_str.zfill(10) # дополняем лидирующими нулями

number = int(input("Введите неотрицательное целое число: "))
print('Восьмеричный код:',to_octal(number))

# Вариант 8.
# 1. Найти все натуральные числа, не превосходящие заданного n, которые
# делятся на каждую из своих цифр.
n = int(input("Введите n: "))
result = []

for num in range(1, n + 1):
    s = str(num)
    if '0' in s: # на ноль делить нельзя
        continue
    if all(num % int(digit) == 0 for digit in s):
        result.append(num)

print('Числа, делящиеся на каждую из своих цифр:',result)

# 2. Ввести одномерный массив A длиной m. Поменять в нём местами первый
# и последний элементы. Длину массива и его элементы ввести с клавиатуры. В
# программе описать процедуру для замены элементов массива. Вывести
# исходные и полученные массивы.
def swap_first_last(arr):
    if len(arr) > 1:
        arr[0], arr[-1] = arr[-1], arr[0]

m = int(input("Введите длину массива: "))
A = [int(input(f"Введите элемент {i + 1}: ")) for i in range(m)]

print("Исходный массив:", A)
swap_first_last(A)
print("Массив после замены:", A)

# Вариант 9.
# 1. Из заданного числа вычли сумму его цифр. Из результата вновь вычли
# сумму его цифр и т. д. Через сколько таких действий получится ноль?
def digit_sum(n):
    return sum(int(d) for d in str(n))

n = int(input("Введите число: "))
steps = 0
while n != 0:
    n -= digit_sum(n)
    steps += 1
print("Количество шагов:", steps)

# 2. Даны 3 различных массива целых чисел. В каждом массиве найти
# произведение элементов и среднеарифметическое значение.
def product(arr):
    result = 1
    for x in arr:
        result *= x
    return result

arrays = []
for i in range(1, 4):
    print('Массив', i)
    arr = list(map(int, input(f"Введите {i}-й массив через пробел: ").split()))
    arrays.append(arr)

for i, arr in enumerate(arrays, 1):
    prod = product(arr)
    avg = average(arr)
    print('Массив', i, ':', arr)
    print('Произведение:', prod)
    print('Среднеарифметическое:', avg)

# Вариант 10.
# 1. На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных
# из цифр а, b, с.
def count_valid_numbers(N, a, b, c):
    count = 0
    valid_digits = {str(a), str(b), str(c)}

    for num in range(100, N + 1):
        num_str = str(num)
        # Проверяем, все ли цифры строки содержатся в valid_digits
        if all(digit in valid_digits for digit in num_str):
            count += 1

    return count


# Ввод данных
N = int(input("Введите N (210 < N < 231): "))
a = int(input("Введите первую цифру a: "))
b = int(input("Введите вторую цифру b: "))
c = int(input("Введите третью цифру c: "))

result = count_valid_numbers(N, a, b, c)
print("Количество чисел:", result)

# 2. Составить программу, которая изменяет последовательность слов в
# строке на обратную.
def reverse_words(s):
    words = s.split()
    return ' '.join(words[::-1])

stroka = input('Введите последовательность слов: ')
result = reverse_words(stroka)
print(result)

# Вариант 11.
# 1. Два простых числа называются «близнецами», если они отличаются друг
# от друга на 2 (например, 41 и 43). Напечатать все пары «близнецов» из отрезка
# [n, 2n], где n — заданное натуральное число, большее 2..
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

n = int(input("Введите n (n > 2): "))

pairs = []
for p in range(n, 2*n - 1):
    if is_prime(p) and is_prime(p + 2):
        pairs.append((p, p + 2))

if pairs:
    print(f"Пары близнецов на отрезке [{n}, {2*n}]:")
    for pair in pairs:
        print(f"{pair[0]} и {pair[1]}")
else:
    print("Пар близнецов не найдено")

# 2. Даны две матрицы А и В. Написать программу, меняющую местами
# максимальные элементы этих матриц. Нахождение максимального элемента
# матрицы оформить в виде процедуры.
def find_max(matrix):
    max_val = matrix[0][0]
    max_i, max_j = 0, 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_val:
                max_val = matrix[i][j]
                max_i, max_j = i, j
    return max_val, max_i, max_j

A = [[int(x) for x in input().split()] for _ in range(int(input()))]
B = [[int(x) for x in input().split()] for _ in range(int(input()))]

# Находим максимумы и меняем местами
max_A, i_A, j_A = find_max(A)
max_B, i_B, j_B = find_max(B)
A[i_A][j_A] = max_B
B[i_B][j_B] = max_A

print('Матрица A')
for row in A:
    print(row)
print('Матрица B')
for row in B:
    print(row)

# Вариант 12.
# 1. Два натуральных числа называются «дружественными», если каждое из
# них равно сумме всех делителей (кроме его самого) другого (например, числа
# 220 и 284). Найти все пары «дружественных» чисел, которые не больше
# данного числа N.
def div_sum(n):
    s = 1 if n > 1 else 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i + (n//i if i != n//i else 0)
    return s

N = int(input('Введите число N '))
for a in range(1, N+1):
    b = div_sum(a)
    if N >= b > a == div_sum(b):
        print(a, b)

# 2. Даны длины сторон треугольника a, b, c. Найти медианы треугольника,
# сторонами которого являются медианы исходного треугольника. Для
# вычисления медианы проведенной к стороне а, использовать формулу
# Вычисление медианы оформить в виде процедуры.
def median(a, b, c):
    return 0.5 * (2*b**2 + 2*c**2 - a**2)**0.5

a, b, c = map(float, input("Введите стороны треугольника: ").split())

# Медианы исходного треугольника
ma = median(a, b, c)
mb = median(b, a, c)
mc = median(c, a, b)

# Медианы нового треугольника
new_ma = median(ma, mb, mc)
new_mb = median(mb, ma, mc)
new_mc = median(mc, ma, mb)
print('Медианы треугольника, сторонами которого ' +
      'являются медианы исходного треугольника:',
      new_ma, new_mb, new_mc)

# Вариант 13.
# 1. Натуральное число, в записи которого n цифр, называется числом
# Армстронга, если сумма его цифр, возведенная в степень n, равна самому
# числу. Найти все числа Армстронга от 1 до к.
def is_armstrong(num):
    str_num = str(num)
    n = len(str_num)
    sum_digits = sum(int(digit) ** n for digit in str_num)
    return sum_digits == num

k = int(input("Введите k: "))
armstrong_numbers = []
for num in range(1, k + 1):
    if is_armstrong(num):
        armstrong_numbers.append(num)

print("Числа Армстронга от 1 до", k, ":", armstrong_numbers)

# 2. Три точки заданы своими координатами X(x1, x2), Y(y1, y2) и Z(z1, z2).
# Найти и напечатать координаты точки, для которой угол между осью абсцисс и
# лучом, соединяющим начало координат с точкой, минимальный. Вычисления
# оформить в виде процедуры.
def angle_to_point(x, y):
    return atan2(y, x)

# Ввод точек
X = tuple(map(float, input("Введите координаты X (через пробел): ").split()))
Y = tuple(map(float, input("Введите координаты Y (через пробел): ").split()))
Z = tuple(map(float, input("Введите координаты Z (через пробел): ").split()))

angles = [
    (angle_to_point(X[0], X[1]), X, "X"),
    (angle_to_point(Y[0], Y[1]), Y, "Y"),
    (angle_to_point(Z[0], Z[1]), Z, "Z")
]

min_angle, point, name = min(angles, key=lambda x: x[0])
print('Точка', name, 'имеет минимальный угол:', point)

# Вариант 14.
# 1. Составить программу для нахождения чисел из интервала [М, N], имеющих
# наибольшее количество делителей.
def count_divisors(n):
    if n <= 0:
        return 0
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2  # Два делителя: i и n//i
    return count


M = int(input("Введите M: "))
N = int(input("Введите N: "))

# Находим число с максимальным количеством делителей
max_divisors = 0
numbers_with_max_divisors = []

for num in range(M, N + 1):
    div_count = count_divisors(num)
    if div_count > max_divisors:
        max_divisors = div_count
        numbers_with_max_divisors = [num]
    elif div_count == max_divisors:
        numbers_with_max_divisors.append(num)

print('Числа из интервала', [{M}, {N}],
      'с наибольшим количеством делителей (',max_divisors,'):'
      ,numbers_with_max_divisors)

# 2. Четыре точки заданы своими координатами X(x1, x2), Y(y1, y2), Z(z1, z2), P(p1,
# p2). Выяснить, какие из них находятся на максимальном расстоянии друг от
# друга и вывести на экран значение этого расстояния. Вычисление расстояния
# между двумя точками оформить в виде процедуры.

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

points = []
for name in ['X', 'Y', 'Z', 'P']:
    coords = list(map(float, input(f"Введите координаты точки {name}: ").split()))
    points.append(coords)

# Максимальное расстояние
max_distance = 0
max_pair = None
for i in range(4):
    for j in range(i + 1, 4):
        dist = distance(points[i], points[j])
        if dist > max_distance:
            max_distance = dist
            max_pair = (points[i], points[j])

print('Максимальное расстояние:', max_distance)
print('Между точками:', max_pair[0],
      'и', max_pair[1])

# Вариант 15.
# 1. Найти все простые натуральные числа, не превосходящие n, двоичная
# запись которых представляет собой палиндром, т. е. читается одинаково слева
# направо и справа налево.
def is_binary_palindrome(n):
    binary = bin(n)[2:]  # Убираем '0b' префикс
    return binary == binary[::-1]

n = int(input("Введите n: "))
result = []
for num in range(2, n + 1):
    if is_prime(num) and is_binary_palindrome(num):
        result.append(num)

if result:
    print("Простые числа, двоичная запись которых является палиндромом:")
    print(result)
else:
    print("Таких чисел нет")

# 2. Четыре точки заданы своими координатами X(x1, x2, x3), Y(y1, y2, y3),
# Z(z1, z2, z3), T(t1,t2, t3). Выяснить, какие из них находятся на минимальном
# расстоянии друг от друга и вывести на экран значение этого расстояния.
# Вычисление расстояния между двумя точками оформить в виде процедуры.
def distance_3d(point1, point2):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

points = []
for name in ['X', 'Y', 'Z', 'T']:
    coords = list(map(float, input(f"Введите координаты точки {name}: ").split()))
    points.append(coords)

# Минимальное расстояние
min_distance = distance_3d(points[0], points[1])  # Начальное значение минимально
min_pair = (points[0], points[1])

for i in range(4):
    for j in range(i + 1, 4):
        dist = distance_3d(points[i], points[j])
        if dist < min_distance:
            min_distance = dist
            min_pair = (points[i], points[j])

print('Минимальное расстояние:', min_distance)
print('Между точками:', min_pair[0],
      'и', min_pair[1])