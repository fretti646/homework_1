import random

'''Задача 1:
Пользователь вводит длину стороны квадрата N и символ CH. 
Программа должна вывести с помощью символа CH 
квадрат со стороной N'''


def square(N: int, CH: str):
	if N >= 1:
		for i in range(1, N ** 2 + 1):
			print(CH, end = ' ')
			if i % N == 0:
				print()


# print(square(3, '*'))


'''Задача 2:
Сгенерировать рандомную последовательность из 5 чисел. 
Диапазон последовательности от 1 до 100. Если все числа в
последовательности больше 50, вывести True, в ином случае False'''


def more_50():
	lst = [random.randint(1, 100) for _ in range(5)]
	print(lst)
	# elem_max = lst[1] # минимальный эл, кот точно есть в этом списке
	for i in lst:
		if i <= 50:
			return False
	return True


# print(more_50())


'''Задача 3: 
Задачу начать решать с пустого списка:
lst = []
Папа написал Саше список продуктов (молоко, огурцы, пиво, рыбка) 
и бабушка тоже попросила купить 
некоторые продукты (чай, сахар, сухарики).
Мама увидела список и сказала вычеркнуть пиво и рыбку
Помоги Саше сформировать единый список покупок 
и посчитать сколько пунктов содержит общий список покупок'''


def shop_lst():
	count = 0
	lst = []
	lst.append('молоко')
	lst.append('огурцы')
	lst.append('пиво')
	lst.append('рыбка')
	lst.append('чай')
	lst.append('сахар')
	lst.append('сухарики')
	lst.remove('пиво')
	lst.remove('рыбка')
	for i in range(len(lst)):
		count += 1
		print(lst[i])
	#print(*lst)
	return count


# print(shop_lst())


'''Задача 4:
Есть список. пользователь 
вводит число. Нужно определить, есть ли это число в списке'''
    

def ch_in_lst(num: int):
	lst = [random.randint(1, 100) for _ in range(10)]
	# lst = [1, 2, 3, 4, 5]
	if num in lst:
		return True
	else:
		return False


# print(ch_in_lst(1))


'''Задача 5:
Есть список и число, которое ввел пользователь
посчитать сколько раз это число встречается в списке'''


def count_num_lst(num: int):
	lst = [random.randint(1, 100) for _ in range(10)]
	# lst = [1, 2, 3, 4, 5, 1, 1, 1]
	count = 0
	for i in range(len(lst)):
		if num == lst[i]:
			count += 1
	return count


print(count_num_lst(3))



