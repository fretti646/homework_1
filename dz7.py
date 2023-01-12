''Задача 1:
Напишите функцию 
read_last(lines: int, file: str)
которая будет открывать определенный файл file 
и возвращать последние lines строк этого файла'''



def read_last(lines: int, file: str):
	f = open(file, encoding = 'utf-8')
	lst =[]
	for row in f:
		lst.append(row)
	lst_last_elem = lst[len(lst)-lines:len(lst)]
	f.close()
	return lst_last_elem

print(read_last(1, './file.txt'))
#print(read_last(2, 'C:/Users/Public/Documents/dz7/file.txt'))
# print(read_last(3, 'C:/..//.//.//.//file.txt'))
# print(read_last(3, './file.txt'))
#C:\Users\Public\Documents\dz7


'''Задача 2:
Документ article.txt содержит следующий текст:

Мороз и солнце день чудесный
Еще ты дремлешь друг прелестный 
Пора красавица проснись
Открой сомкнуты негой взоры
Навстречу северной Авроры
Звездою севера явись
 
Требуется реализовать функцию 
longest_words(file: str)
которая возвращает слово или список слов (если таковых несколько), 
которые имеют максимальную длину
(или список из 1 слова)'''


def longest_words(file: str):
	f = open(file, encoding = 'utf-8')
	s = f.read()
	lst = s.split()
	f.close()
	len_s = 0
	max_len_lst = []
	for i in lst:
		if len(i) > len_s:
			max_len_lst = []
			len_s = len(i)
			max_len_lst.append(i)
		elif len(i) == len_s:
			max_len_lst.append(i)
	return max_len_lst


print(longest_words('./article.txt'))

# print(longest_words('C:/Users/Public/Documents/dz7/article.txt'))


'''Задача 3:
Имеется текстовый файл prices.txt с информацией о заказе из 
интернет магазина. В нем каждая строка с помощью символа табуляции \t
разделена на три колонки:
- наименование товара;
- количество товара (целое число);
- цена (в рублях) товара за 1 шт. (целое число).
Напишите функцию
get_basket_amount(file: str) -> int
которая подсчитываюет общую стоимость заказа и возвращает сумму заказа'''


def get_basket_amount(file: str) -> int:
	f = open(file, encoding = 'utf-8')
	s = f.read()
	
	lst = s.split('\n')
	f.close()
	len_lst = []
	summ = 0
	#print(lst)
	for i in lst:
		if i == '':
			continue
		len_lst =  i.split()
		summ += int(len_lst[1]) * int(len_lst[2])
	return summ


print(get_basket_amount('./prices.txt'))


