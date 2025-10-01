print('№1')
n = int(input("Введите число n: "))
print('Все квадраты натуральных чисел, не превосходящие N')
i = 1
while i * i <= n:
    print(i * i)
    i += 1


print('№2')
n = int(input("Введите число n: "))
delitel = 2
while delitel <= n and n % delitel != 0:
    delitel += 1

print('Наименьший натуральный делитель числа n, отличный от 1')
print(delitel)


print('№3')
n = int(input("Введите число n: "))
e = 2
stepen = 1
while e * 2 <= n:
    e *= 2
    stepen += 1

print("Наибольшая целая степень двойки, не превосходящая N\n" +
      "Показатель степени", stepen, "\n"
      "Значение степени",e)


print('№4')
def zadanie_4(x, y):
    den = 1
    while y > x:
        x *= 1.1
        den += 1
    return den

x = int(input("В первый день спортсмен пробежал километров: "))
y = int(input("Минимальное количество километров: "))
print("Номер дня, на который пробег спортсмена составит не менее",
      y,"километров: ", zadanie_4(x,y))


print('№5')
kol_chlenov_posledovat = 0
while True:
    e = int(input("Введите целое неотрицательное число: "))
    if e >= 0:
        if e == 0:
            break
        else:
            kol_chlenov_posledovat += 1

print("Количество членов последовательности:", kol_chlenov_posledovat)


print('№6')
kol_chlenov_posledovat = 0
summa = 0
while True:
    e = float(input("Введите число: "))
    if e == 0:
        break
    else:
        kol_chlenov_posledovat += 1
        summa += e    

print("Среднее значение всех элементов последовательности:", summa/kol_chlenov_posledovat)


print('№7')
kol_chlenov_posledovat = 0
predidushiy = 0
while True:
    e = int(input("Введите натуральное число: "))
    if e >= 0:
        predidushiy = e
        if e == 0:
            break
        elif e > predidushiy:
            kol_chlenov_posledovat += 1

print("Элементов этой последовательности больше предыдущего элемента",
      kol_chlenov_posledovat)


print('№8')
count = 1
max_count = 0 
previous_number = 0  

while True:
    number = int(input("Введите натуральное число: "))
    if number == 0:
        break
    if previous_number == 0:
        previous_number = number
    elif number == previous_number:
        count += 1 
    else:
        max_count = max(count, max_count)
        count = 1  
        previous_number = number

max_count = max(count, max_count)

print("Наибольшее количество подряд идущих одинаковых элементов:", max_count)
