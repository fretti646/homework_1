'''
s = input('Введите строку:')
s = s.lower()
lst = s.split() # преобразует строку в список
d = {}
for i in lst:
	if not i in d:
		d[i] = 1
	else:
		d[i] += 1
for key in d.keys():
	print(key, d[key], end = ' | ')
print()
'''

