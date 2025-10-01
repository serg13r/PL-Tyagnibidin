print('№1')
A = 1 
B = 10
for i in range(A,B+1):
    print(i)


print('№2')
A = 10
B = 1
if A < B:
    for i in range(A,B+1):
        print(i)
else:
    for i in range(A,B-1,-1):
        print(i)


print('№3')
A = 10 
B = 1
for i in range(A,B-1,-1):
    if i % 5 != 0:    
        print(i)


print('№4')
s = 0
for _ in range(1, int(input('Введите число N '))+1):
    s += int(input('Введите число '))
print('Сумма чисел',s)


print('№5')
e = 0 
for i in range(1, int(input('Введите натуральное число N '))+1):
    e += i**3
print(e)


print('№6')
f = 1 
for i in range(1, int(input('Введите по которому нужно вывести факториал '))+1):
    f *= i
print(f)


print('№7')
n = int(input("Введите число n: "))
total_sum = 0  
current_fact = 1   
for i in range(1, n + 1):    
    current_fact *= i        
    total_sum += current_fact  
print("Сумма факториалов от 1 до", n, ":", total_sum)


print('№8')
n = int(input("Введите число n (До 9 включительно, натуральное):"))
if n > 9 or n < 0: 
    print('Число n не подходит под условия')
for i in range(1, n + 1):
    print(''.join(map(str, range(1, i + 1))))


print('№9')
n = int(input("Введите число n (количество чисел из ряда Фибоначчи):"))
a, b = 0, 1
sum_fibonacci = a
for _ in range(n - 1):
    sum_fibonacci += b
    a, b = b, a + b

print("Сумма первых", n, "чисел ряда Фибоначчи:", sum_fibonacci)


print('№10')
N = int(input("Введите количество чисел из ряда Фибоначчи: "))
K = int(input("Введите стартовый индекс: "))

a, b = 0, 1
for _ in range(K - 1):
    a, b = b, a + b

sum_fibonacci = 0
for _ in range(N):
    sum_fibonacci += a
    a, b = b, a + b

print("Сумма", N, "чисел ряда Фибоначчи, начиная с", K, ":", sum_fibonacci)