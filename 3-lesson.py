
import random

def af(a, b, l, N):
    return (l*2)+(2*(b*(N-1)))+(2*(a*N)-a)

def find_min(a, b, c):
    return min(a, b, c)


print('№1 ')

a = int(input('Введите первое число'))
a += int(input('Введите второе число'))
a += int(input('Введите третье число'))

print('Сумма чисел = ', a)


print('№2 ')

a = int(input('Введите длину первого катета'))
a *= int(input('Введите длину второго катета'))

print('Сумма чисел = ', a * 0.5)


print('№3 ')

n = random.randint(0,9000)
if n // 60 <= 24:
    print("количество часов: ", n // 60 - 1, ", количество минут: ",  n % 60 - 1)
else:
    print("количество часов: ", (n // 60) % 24  - 1, ", количество минут: ",  n % 60 - 1)

print('№4 ')

a = int(input("Расстояние между рядами: "))
b = int(input("Расстояние между дырочками: "))
l = int(input("Дырочек в ряду: "))
N = int(input("Длина свободного шнурка: "))

print(af(a,b,l,N))


print('№5 ')

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print(f"Наименьшее число: ",find_min(a, b, c))


print('№6 ')

print('Получение координат клеток ')

x1, y1 = map(int, input("Введите номер столбца и номер строки для первой клетки (через пробел) ").split())
x2, y2 = map(int, input("Введите номер столбца и номер строки для второй клетки (через пробел) ").split())

if ((x1 + y1) % 2 == (x2 + y2) % 2):
    print('Да')
else:
    print('Нет')


print('№7 ')

year = int(input("Введите год "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год невисокосный") 


print('№8 ')

a, b, c = map(int, input("Ввод трех чисел (через пробел) ").split())

if a == b == c:
    print(3, "Все три числа равны") 
elif a == b or b == c or a == c:
    print(2, "Ровно два числа равны")
else:
    print(0, "Все числа различны")


print("№9 ")

n, m, k = map(int, input("Ввод трех чисел (через пробел) ").split())

if (n * m) % k == 0:
    print("Можно отломить")
else:
    print("Нельзя отломить")
