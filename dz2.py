# задача 1
'''
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
c = int(input('Ваш предполагаемый результат вычисления:'))
if a * b == c:
	print('Все верно! Вы правы!')
else:
	print('Подумайте еще...')
'''

# задача 2
'''
a = int(input('Для отображения расписания введите номер дня недели:'))
if a == 1:
	print('Понедельник. 1.Сопромат(лекция) 2.Гидравлика(лекция)')
elif a == 2:
	print('Вторник. 1.ТПС(лекция) 2.Отопление(практика) 3.ЦТС')
elif a == 3:
	print('Среда. 1.Сопромат(лаб.) 2.Отопление(лекция) 3.ТПС(лекция)')
elif a == 4:
	print('Четверг. Выходной')
elif a == 5:
	print('Пятница. 1.Электротехника 2. Электротехника. 3.Электротехника')
elif a == 6:
	print('Суббота. Выходной')
elif a == 7:
	print('Воскресенье. Выходной')
else:
	print('введите число от 1 до 7')
'''

# задача 4
'''
num_1 = int(input('Введите число:'))
if -99 <= num_1 <= -10 or 10 <= num_1 <= 99:
	print('Число двузначное')
else:
	print('Число не двузначное')
'''

# задача 3 (1. not, 2. and, 3. or), (ОТВЕТ TRUE)
'''
x = 5
y = 10
print(y > x * x or y >= 2 * x and x < y)
'''

# задача 5

num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
num_3 = int(input('Введите третье число:'))
if num_1 > num_2 and num_1 > num_3:
	print(num_1)
elif num_2 > num_1 and num_2 > num_3:
	print(num_2)
elif num_3 > num_1 and num_3 > num_2:
	print(num_3)
elif num_3 == num_1 or num_3 == num_2 or num_2 == num_1:
	print('все числа равны')

# задача 6
'''
num_1 = int(input('Введите первое число:'))
num_2 = int(input('Введите второе число:'))
a = str(input('Операция(+, -, /, *, mod, pow, div):'))
if a == '+':
	print(num_1 + num_2)
elif a == '-':
	print(num_1 - num_2)
elif a == '/':
	print(num_1 / num_2)
elif a == '*':
	print(num_1 * num_2)
elif a == 'mod':
	print(num_1 % num_2)
elif a == 'pow':
	print(num_1 ** num_2)
elif a == 'div':
	print(num_1 // num_2)
'''

# задача 7
'''
a = int(input('Введите первое число:'))
b = int(input('Введите второе число:'))
if a % b == 0:
	print('число a делится на число b.')
elif b % a == 0:
	print('число b делится на число a.')
else:
	print('Числа a и b не делятся друг на друга.')
'''
# задача 8
'''
num = int(input('Введите трехзначное число:'))
c = (num % 10**1) // 10**0
b = (num % 10**2) // 10**1
a = (num % 10**3) // 10**2
if a == b == c:
	print('В вашем числе все цифры одинаковые!')
elif a == b or a == c or b == c:
	print('В вашем числе две цифры одинаковые!')
else:
	print('В вашем числе нет одинаковых цифр!')
'''
