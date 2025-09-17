print('№1 ','Курс Основы программирования начался')

print('№2 ', 16823 * 12302 / 3092 % 1)

age = 18 # int(input())
name = 'Не Иван' # input()
if 75 > age > 0:
    if name != 'Иван':
        if age >= 16:
            print('№3 ','Поздравляем вы поступили в ВГУИТ')
        else:
            print('Сначала нужно окончить школу!')
            print('Осталось ',16-age,' лет')

seconds = 19038783
print('№4 ',f"Дни {int(seconds/60/60/24)} Часы: {int(seconds/60/60)} Минуты: {int(seconds/60)} Секунды: {int(seconds)}")

n = '9'
nn = int(n)
print('№5 ',nn + nn**2 + nn**3 + nn**4 + nn**5)

x, y = 0,1
x,y = y,x
print('№6 ',x,y)

number = 9
if number % 2 == 0:
    print('Чётное')
else:
    print('№7 ','Нечётное')
