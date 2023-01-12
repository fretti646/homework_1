# задача 1 (Green Red Blue RedRedGreen BlueGreen Green)
'''
r = 'Red' 
g = 'Green' 
b = 'Blue' 
print(g, r , b, r + r + g, b + g, g)
'''
# задача 2
'''
name = input('Ваше имя:')
surname = input('Ваша фамилия:')
eat = input('Укажите Ваше любимое блюдо:')
print('Пользователь', name, surname, 'любит есть', eat+'.', 'Порадуемся за него!')
'''
# задача 3 (забыла, как сделать длинное тире, например, Екатеринбург-Каменск-Уральский странно выглядит)
'''
one = input('Пункт вашего отправления:')
two = input('Пункт вашего прибытия:')
print(one+'-'+two)
'''
# задача 4 ?
'''
a = input('First word: ') 
b = input('Second word: ') 
print(a, b) 
temp=a
a=b 
b=temp
print(a, b) 
'''
# задача 5
'''
num_1 = (input('Введите первое число:'))
num_2 = (input('Введите второе число:'))
one = int(num_1) % 100
two = int(num_2) % 100
print('Ответ:', one + two)
'''
# задача 6
'''
num = int(input('Введите число:'))
a = (num % 10**1) // 10**0
b = (num % 10**2) // 10**1
c = (num % 10**3) // 10**2
d = (num % 10**4) // 10**3
print('Обратное число:', a, b, c, d, sep='')
'''
