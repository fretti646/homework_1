# задача 1
# '''Сигнатура: k_isalpha(s: str) -> bool
# Написать свою реализацию функции isalpha()
# состоит ли из букв'''
# def k_isalpha(s: str) -> bool:
# 	i = 0
# 	while i < len(s):
# 		if s[i] >= 'a' and s[i] <= 'z':
# 			i += 1
# 		elif s[i] >= 'A' and s[i] <= 'Z':
# 			i += 1
# 		elif s[i] >= 'а' and s[i] <= 'я':
# 			i += 1
# 		elif s[i] >= 'А' and s[i] <= 'Я':
# 			i += 1
# 		else:
# 			return False
# 	return True


# k_isalpha('sfsdsd')
# print(k_isalpha('fffffffффффффф'))


# задача 2
'''Сигнатура: k_islower(s: str) -> bool
Написать свою реализацию функции islower
возвращает True , если все символы в строке имеют 
нижний регистр (строчные), при этом строка не должна быть пустой,
 то есть должна иметь хотя бы один символ в нижнем регистре
и не состоять из одних пробелов()'''
def k_islower(s: str) -> bool:
	i = 0
	count_space = 0
	count_low_reg = 0
	count_up_reg = 0
	count_num = 0
	while i < len(s):
		if s[i] == ' ':
			count_space += 1
		elif 'a' <= s[i] <= 'z':
			count_low_reg += 1
		elif 'я' <= s[i] <= 'а':
			count_low_reg += 1
		elif 'A' <= s[i] <= 'Z':
			count_up_reg += 1
		elif 'А' <= s[i] <= 'Я':
			count_up_reg += 1
		elif '0' <= s[i] <= '9':
			count_num += 1 
		i += 1
	if count_low_reg == 0 :
		return False
	elif count_up_reg > 0:
		return False
	elif count_space == len(s):
		return False
	elif count_num == len(s):
		return False
	else:
		return True
	
	# if count_space == len(s):
	# 	return False
	# while i < len(s):	
	# 	if s[i] >= 'A' and s[i] <= 'Z':
	# 		return False
	# 	elif s[i] >= 'А' and s[i] <= 'Я':
	# 		return False
	# 	else:
	# 		i += 1
	#return True

# def k_islower(s):
#     i = 0
#     Flag = True
    
#     while(i < len(s)):
#         Flag = True
#         if(ord("A") <= ord(s[i]) <= ord("Z") ):
#             Flag = False
#             break
#         elif(ord("А") <= ord(s[i]) <= ord("Я")):
#             Flag = False
#             break
#         i += 1
#     return(Flag)


#print(k_islower('1'))


# задача 3
'''Сигнатура: k_istitle(s: str) -> bool
Написать свою реализацию функции istitle()
если каждое слово в строке str начинается с 
заглавной буквы и в ней есть хотя бы один символ в верхнем регистре'''
# def k_istitle(s: str) -> bool:
# 	i = 1
# 	if not 'А' <= s[0] <= 'Я':
# 		return False
# 	elif not 'A' <= s[0] <= 'Z':
# 		return False
# 	elif s[0] == ' ':
# 		return False 
# 	if 'A' <= s[0] <= 'Z':
# 		while i < len(s):
# 			if 'a' <= s[i] <= 'z':
# 				i += 1
# 			elif 'а' <= s[i] <= 'я':
# 				i += 1
# 			else:
# 				return False
# 	elif 'А' <= s[0] <= 'Я':
# 		while i < len(s):
# 			if 'а' <= s[i] <= 'я':
# 				i += 1
# 			elif 'a' <= s[i] <= 'z':
# 				i += 1
# 			else:
# 				return False
# 	return True


# def k_istitle(s: str) -> bool:
# 	i = 0 
# 	while i < len(s):
# 		if s[0] == ' ':
# 			i += 1
# 		elif 'A' <= s[i] <= 'Z':
# 			i += 1
# 			while i < len(s):
# 				if 'a' <= s[i] <= 'z':
# 					i += 1
# 				elif 'а' <= s[i] <= 'я':
# 					i += 1
# 				else:
# 					return False
# 		elif 'А' <= s[i] <= 'Я':
# 			while i < len(s):
# 				if 'a' <= s[i] <= 'z':
# 					i+= 1
# 				elif 'а' <= s[i] <= 'я':
# 					i += 1
# 				else:
# 					return False
				
				
# 	return True

			
# print(k_istitle('Aed'))


# задача 4
'''Сигнатура: k_upper(s: str) -> str
Написать свою реализацию функции upper()
превращает весь нижний регистр в верхний'''
# def k_upper(s: str) -> str:
# 	i = 0
# 	s_new = ''
# 	while i < len (s):
# 		if 'a' <= s[i] <= 'z':
# 			new_ch = ord(s[i]) - 32
# 			s_new += chr(new_ch)
# 			i += 1
# 		elif 'а' <= s[i] <= 'я':
# 			new_ch = ord(s[i]) -32
# 			s_new += chr(new_ch)
# 			i += 1
# 		else:
# 			s_new += s[i]
# 			i += 1
# 	return(s_new)


# print(k_upper('bfcifciudwceicw212313unucbdy/////'))


# задача 5
'''Сигнатура: k_endswith(s: str, substring: str) -> bool
Написать свою реализацию функции endswith()
заканчивается ли строка символами указанными в скобках'''
# def k_endswith(s: str, substring: str) -> bool:
# 	i = 0
# 	s = s[: : -1]
# 	substring = substring[: : -1]
# 	while i < len(substring):
# 		if s[i] == substring[i]:
# 			i += 1
# 		else:
# 			return False
# 	return True


# print(k_endwith('qwerty', 'rty'))


# задача 6
'''Сигнатура: k_count(s: str, substring: str) -> int
Написать свою реализацию функции count()
возвращает количество вхождений подстроки sub в строку str
 в диапазоне индексов [start, end] , если они переданы в метод.'''
# def k_count(s: str, substring: str) -> int:
# 	i = 0
# 	count = 0
# 	if substring == '':
# 		count = 1 + len(s)
# 	else:
# 		while i < len(s):
# 			if s[i] == substring:
# 				count += 1
# 			i += 1
# 	return count


# print(k_count('dddd', ''))
# print('    aaas'.count(' '))


# задача 7
'''Сигнатура: k_strip(s: str) -> str
Написать свою реализацию функции strip()
удаляет в начале (перед текстом) и в конце (после текста) строки пробелы (в середине оставляет)'''
# def k_strip(s: str) -> str:
# 	#s1 = s[::-1]
# 	i = 0
# 	count1 = 0 
# 	s = s.replace('\t',' ')
# 	if s[0] ==  ' ':
# 		while s[i] ==  ' ':
# 			count1 += 1
# 			i += 1
# 		#s = s[count:]
# 	i = 0
# 	count2 = 0
# 	s1 = s[::-1]
# 	if s1[0] == ' ':
# 		while s1[i] ==  ' ':
# 			count2 += 1
# 			i += 1
# 	if count1 != 0 and count2 == 0:
# 		s = s[count1:]
# 	elif count1 == 0 and count2 != 0:
# 		s = s[0:count2 + 1]
# 	elif count1 != 0 and count2 != 0:
# 		s = s[count1:len(s) - count2 ]
# 		# if s[-1] == 't':
# 		# 	s = s[0: len(s) - 2]
# 	return s


# print("тута")
# print(k_strip(' AAs\t  '))


# задача 8
'''Сигнатура: k_replace(s: str, oldvalue(символ, который был): str, newvalue(символ, которым заменяем): str, count(столько раз заменяем): int) -> str
Написать свою реализацию функции replace()
возвращает новую строку с некоторыми или всеми сопоставлениями с шаблоном, заменёнными на заменитель. '''
# def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
# 	s_new = ''
# 	count_new = 0
# 	while i < len(s):
# 		if s[i] == oldvalue and count_new != count:
# 			s_new += newvalue
# 		else:
# 			s_new += s[i]
# 	return s_new

# def k_replace(s: str, oldvalue: str, newvalue: str, count: int) -> str:
#     i = 0
#     count_new = 0
#     s1 = ''
#     s_new = ''
#     #s1 = s[0:len(substring)]
#     while i < len(s):
#         if count == count_new:
#             s_new += s[i: : ]
#             break #  полный выход из цикла (по условию)
#         else:
#             if s[i] != oldvalue[0]:
#                 s_new += s[i]
#             else:
#                 s1 = s[i:i + len(oldvalue)]
#                 if s1 == oldvalue:
#                     s_new += newvalue
#                     i += len(oldvalue) - 1
#                     count_new += 1
#         i += 1
#     return s_new 

# print(k_replace('hello', 'hello', '@@', 1))








