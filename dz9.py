# Практика:

# Файл log_100.json:
# 1) чему равен общий вклад топ-3 всех IP по количеству посещений? Указать процентом
# 2) сколько в файле уникальных IP, с которых на сайт заходили только 1 раз


import json

lst_ip = []
with open('log_100.json') as f:
	j = json.load(f)
for elem in j:
	lst_ip.append(elem['ip'])
d = {}
for i in lst_ip:
	if not(i in d):
		d[i] = 1
	else:
		d[i] += 1
lst_count = []
for value in d.values():
	lst_count.append(value)
lst_count = sorted(lst_count)
count_t_1 = 0
lst_count_top_3 = lst_count[len(lst_count)- 3: ]
summ_top_3 = sum(lst_count_top_3)
count = sum(lst_count)
for elem in lst_count:
	if elem == 1:
		count_t_1 += 1

print('столько в файле уникальных IP, с которых на сайт заходили только 1 раз:', count_t_1)
print('общий вклад топ-3 всех IP по количеству посещений, %:', summ_top_3 *  100 / count)


# Файл log_full.csv:
# 5) найти максимально часто встречающийся IP
# 6) посчитать в процентах вклад этого IP адреса в общее кол-во запросов 
# 7) найти последнюю запись в логах с этим IP и выяснить какой user-agent был у этой записи
# получить словарь:

# suspicious_agent = {
#     "ip": '...',            # самый частовстречаемый ip в логах
#     'fraction': 70.205,     # процент запросов с таким ip от общего кол-ва запросов
#     'count': 29427,         # число запросов с таким IP
#     'last': {               # вложенный словарь с 2-мя полями
#         'agent': '...',     # последний user-agent для этого ip
#         'timestamp': '...', # последний timestap для этого ip
#     }
# }

# запись
# with open('test.csv', 'a') as f:
#     writer = csv.writer(f)
#     writer.writerows(rows)

# чтение:
# rows = []
# with open('test.csv') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         rows.append(row)
#         print(row)
# print(rows)


import csv

OBOBOBrows = [] #строки 
with open ('log_full.csv') as f:
	readed = csv.reader(f) # перевели csv в объект питона
OBOBOB	for row in readed:
		 rows.append(row)
OBOBOB
OBOBOBrows_0 = rows[0]
rows_1_and = rows[1:]
OBOBOBOBOBOBlst_ip = []
OBOBOB
OBOBOBfor i in range(len(rows_1_and)):
	lst_ip.append(rows_1_and[i][1])
OBOBOB
OBOBOBd1 = {}
for i in lst_ip:
	if not (i in d1):
OBOBOB		d1[i] = 1
	else:
		d1[i] += 1

lst_count = []
for value in d1.values():
	lst_count.append(value)

lst_count = sorted(lst_count) # сортировка списка
count = sum(lst_count) # сумма всех посещений
max_times = max(lst_count) # макс число посещений одного айпи

for key, value in d1.items(): # позволяет бегать по ключу и переменной
	if value == max_times: # сравниваем значения словаря с максимальным значением посещений
		max_ip = key # запоминаем айпи с максимальным колличеством посещений
		break # прерываем цикл, так как все нашли

procent = (max_times * 100 / count, 3)

lst_max_ip = []
for i in range(len(rows_1_and)):
	if rows_1_and[i][1] == max_ip:
		lst_max_ip.append(rows_1_and[i]) # вся информация с популярным айпи

last = {				# вложенный словарь с 2-мя полями
rows_0[2]:lst_max_ip[len(lst_max_ip) - 1][2],	# последний user-agent для этого ip
rows_0[0]:lst_max_ip[len(lst_max_ip) - 1][0]		# последний timestap для этого ip
}

suspicious_agent = {
    "ip": max_ip,            # самый частовстречаемый ip в логах
    'fraction': procent,     # процент запросов с таким ip от общего кол-ва запросов
    'count': max_times,         # число запросов с таким IP
    'last': last
}

print(suspicious_agent)







