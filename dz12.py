# 1) Реализация класса "Карточная игра",
# который будет содержать методы
# для создания колоды карт, раздачи карт игрокам, сравнения карт и т.д.

import random

class Card_Game:
    # В классе реализована раздача и сравнение карт по правилам игры "Дурак подкидной"
    def __init__(self, quan_of_cards_in_deck, quan_of_players) -> None:
        self.quan_of_cards_in_deck = quan_of_cards_in_deck
        self.quan_of_players = quan_of_players
        self.deck_of_cards = []
        self.ranks = []
        self.suits = []
        self.list_players_and_card = []
        #self.dict_one_card ={}
    
    # Функция создания колоды
    def create_deck_of_cards(self):
       
        hierarchy = 1 # Иерархия карт по рангам
        counter = 0 # Счетчик для установки иерархии карт(меняется каждые 4, т.е. у 6ок иерархия 1, у 7ок иерархия 2 и т.д.)
        self.suits = ["clubs", "spades", "hearts", "diamonds"] # Список мастей
        dict_one_card ={} #Словарь с полной инфой по карте
        num_card = 0 # Порядковый номер карты
      
        # Список рангов, взависимости от выбранного объема колоды
        if not self.quan_of_cards_in_deck in [36, 52, 54]:
            print("Указаное неверное количество карт в колоде (Нужно выбрать 36, 52 или 54 карты)")
        else:
            if self.quan_of_cards_in_deck == 36:
                self.ranks = ["6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            elif self.quan_of_cards_in_deck == 52 or self.quan_of_cards_in_deck == 54:
                self.ranks = ["2", "3", "4", "5","6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
            
            for i in self.ranks:
                for j in self.suits:
                    num_card += 1
                    dict_one_card ={}
                    dict_one_card["num_card"] = num_card
                    dict_one_card["full_name"] = i + " of " + j
                    dict_one_card["suit"] = j
                    dict_one_card["rank"] = i
                    dict_one_card["hierarchy"] = hierarchy
                    dict_one_card["trump"] = 0
                    counter += 1
                    if counter % 4 == 0:
                        hierarchy += 1
                    self.deck_of_cards.append(dict_one_card)
                  
            if self.quan_of_cards_in_deck == 54:
                num_card += 1
                dict_one_card ={}
                dict_one_card["num_card"] = num_card
                dict_one_card["full_name"] = "Black Joker"
                dict_one_card["suit"] = "Black"
                dict_one_card["rank"] = "Joker"
                dict_one_card["hierarchy"] = 14
                dict_one_card["trump"] = 0
                self.deck_of_cards.append(dict_one_card)

                num_card += 1
                dict_one_card ={}
                dict_one_card["num_card"] = num_card
                dict_one_card["full_name"] = "Red Joker"
                dict_one_card["suit"] = "Red"
                dict_one_card["rank"] = "Joker"
                dict_one_card["hierarchy"] = 15
                dict_one_card["trump"] = 0
                self.deck_of_cards.append(dict_one_card)
                
            print(self.deck_of_cards)

    # Функция перетасовки колоды
    def shuffle_the_deck(self):
        quan_of_shuffles = random.randint(10, 50)
        for i in range(quan_of_shuffles):
            random.shuffle (self.deck_of_cards)
        print(self.deck_of_cards)
    
    # Функция раздачи карт
    def deal_cards(self):
        if self.quan_of_players == 1:
            print("Игра предназначена для двух и более игроков. Задайте количество игроков более двух.")
        elif self.quan_of_players * 6 > self.quan_of_cards_in_deck:
            print("Слишком много игроков для данного размера колоды")
        else:
            counter_player = 1
            counter_card = 1
            # Определение козырной масти
            trump = self.deck_of_cards[self.quan_of_players * 6]["suit"]
            print(trump)
            
            # Заполнение признака trump, если карта козырная
            for i in range(len(self.deck_of_cards)):
                if self.deck_of_cards[i]["suit"] == trump:
                    self.deck_of_cards[i]["trump"] = 1

            print(self.deck_of_cards)
            
            
            # Алгоритм раздачи
            self.list_players_and_card = []
            for i in range(self.quan_of_players):
                self.list_players_and_card.append([])
            
            print(self.list_players_and_card)
            i = 0
            
            while i < self.quan_of_cards_in_deck:
                for j in range(len(self.list_players_and_card)):
                    self.list_players_and_card[j].append(self.deck_of_cards[i])
                    i += 1
                if(len(self.list_players_and_card[0]) == 6):
                    break
            print(self.list_players_and_card)
    
    # Функция сравнения карт
    def compare_cards(self, first_card, second_card):
        if first_card["hierarchy"] == 15:# Красный Джокер кроет всех
            print(first_card["full_name"], "кроет", second_card["full_name"])
        elif second_card["hierarchy"] == 15:# Красный Джокер кроет всех
            print(second_card["full_name"], "кроет", first_card["full_name"])
        elif first_card["hierarchy"] == 14: # Черный Джокер кроет всех кроме Красного Джокера
             print(first_card["full_name"], "кроет", second_card["full_name"])
        elif second_card["hierarchy"] == 14: # Черный Джокер кроет всех кроме Красного Джокера
             print(second_card["full_name"], "кроет", first_card["full_name"])
        elif first_card["trump"] == 1 and second_card["trump"] != 1 : # Козырная карта кроет некозырную
             print(first_card["full_name"], "кроет", second_card["full_name"])
        elif second_card["trump"] == 1 and first_card["trump"] != 1 : # Козырная карта кроет некозырную
             print(second_card["full_name"], "кроет", first_card["full_name"])
        elif first_card["trump"] == second_card["trump"]: # Сравнение двух козырных или двух некозырных карт
            if first_card["suit"] != second_card["suit"]:
                print("Карты не взаимодействуют в данной игре")
            elif first_card["hierarchy"] > second_card["hierarchy"]:
                print(first_card["full_name"], "кроет", second_card["full_name"])
            elif first_card["hierarchy"] < second_card["hierarchy"]:
                print(second_card["full_name"], "кроет", first_card["full_name"])
        
                
                
        
# 2) Реализация класса "Магазин", который будет содержать информацию о товарах, 
# их ценах, количестве на складе и т.д. и методы для работы с этой информацией,
# такие как добавление/удаление товаров, проведение продаж, поиск товаров по цене и т.д.

class Shop:
    
    def __init__(self) -> None:
        # Задаем начальный список товаров
        self.list_products = [{"name_product" : "product1", "price" : 1000, "quantity_in_stock" : 10, "discount_percent" : 0 },
                             {"name_product" : "product2", "price" : 500, "quantity_in_stock" : 100, "discount_percent" : 10 },
                             {"name_product" : "product3", "price" : 400, "quantity_in_stock" : 20, "discount_percent" : 20 },
                             {"name_product" : "product4", "price" : 200, "quantity_in_stock" : 0, "discount_percent" : 0 }]
        self.list_search_result = []
   
    #Поиск по имени
    def search_by_name(self, name_prod):
        self.list_search_result = []
        for i in range(len(self.list_products)):
            if self.list_products[i]["name_product"] == name_prod:
                self.list_search_result.append(self.list_products[i])
        print(self.list_search_result)
   
    # Поиск по цене            
    def search_by_price(self, min_price, max_price):
        self.list_search_result = []
        for i in range(len(self.list_products)):
            if self.list_products[i]["price"] >= min_price and self.list_products[i]["price"] <= max_price:
                self.list_search_result.append(self.list_products[i])
        print(self.list_search_result)

    # Поиск по наличию на складе
    def search_by_quantity_in_stock(self):
        self.list_search_result = []
        for i in range(len(self.list_products)):
            if self.list_products[i]["quantity_in_stock"] > 0:
                self.list_search_result.append(self.list_products[i])
        print(self.list_search_result)

    # Поиск по наличию скидки
    def search_by_discount(self):
        self.list_search_result = []
        for i in range(len(self.list_products)):
            if self.list_products[i]["discount_percent"] > 0:
                self.list_search_result.append(self.list_products[i])
        print(self.list_search_result)
        
    # Добавление товара
    def add_product(self, name_product , price, quantity_in_stock, discount_percent):
        d = {"name_product" : name_product, "price" : price, "quantity_in_stock" : quantity_in_stock, "discount_percent" :discount_percent }
        self.list_products.append(d)
    
    # Удаление товара
    def del_product(self, name_prod):
        for i in range(len(self.list_products)):
            if self.list_products[i]["name_product"] == name_prod:
                self.list_products.pop(i)
                break
                
    # Продажа товара
    def sale_product(self, name_prod, quantity):
        for i in range(len(self.list_products)):
            if self.list_products[i]["name_product"] == name_prod:
                if self.list_products[i]["quantity_in_stock"] < quantity:
                    print("Данный товар не доступен в данном количестве. Всего на складе:", str(self.list_products[i]["quantity_in_stock"]),"шт")
                else:
                    print("Общая сумма заказа", str(self.list_products[i]["price"] * (1 - self.list_products[i]["discount_percent"] / 100)  * quantity))
                break
        else:
            print("Данного товара не существует")

# 3) Реализовать алгоритм Дейкстры для нахождения кратчайшего пути в графе       
import math 

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
  
    # Печать получившихся минимальных расстояний
    def print_result(self, dist):
        print(dist)

 
     # Вспомогательная функция для поиска вершины с
     # минимальным значением расстояния от набора вершин
     # еще не включеной в дерево кратчайших путей
    def minDistance(self, dist, check_set):
        min_dist = math.inf
 
        #Ищем не ближайшую вершину, которой нет в дереве кратчайших путей
        for v in range(self.V):
            if dist[v] < min_dist and check_set[v] == False:
                min_dist = dist[v]
                min_index = v
 
        return min_index
 
     # Функция, реализующая
     # алгоритм Дейкстры поиска кратчайшего пути для представленного графа
     # Передаем, от какой вершины хотим использовать алгоритм
    def dijkstra(self, start):
        
        dist = [math.inf] * self.V # Создаем список расстояний. Задаем бесконечные расстояния
        dist[start] = 0 # Задаем начальное расстояние
        
#         Создем набор  check_set
#         который отслеживает вершины, включенные в дерево кратчайших путей,
#         т.е. минимальное расстояние которых от источника вычисляется и завершается. Изначально этот набор пуст.
        check_set = [False] * self.V 
 
        for j in range(self.V):
 
           # Выбираем вершину минимального расстояния из набора еще не обработанных вершин.
            u = self.minDistance(dist, check_set)
 
            #Помещаем вершину минимального расстояния в дерево кратчайших путей
            check_set[u] = True
 
             # Обновляем значение расстояния соседних вершин для
             # выбранной вершины, только если текущее
             # расстояние больше нового расстояния и
             # вершина не в дереве кратчайших путей
            for v in range(self.V):
                if (self.graph[u][v] > 0 and check_set[v] == False and dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
 
        self.print_result(dist)

# На вход подается количество вершин
g = Graph(6)
# Описание графа через матрицу смежности
g.graph = [[0, 3, 1, 3, 0, 0],
     [3, 0, 4, 0, 0, 0],
     [1, 4, 0, 0, 7, 5],
     [3, 0, 0, 0, 0, 2],
     [0, 0, 7, 0, 0, 4],
     [0, 0, 5, 2, 4, 0]]

# Применение алгоритма 
g.dijkstra(0)
