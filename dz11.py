# 1) Название: создание класса пиво

# Задача: разработать класс, который представляет собой экземпляр пива.

# Функциональные требования: 
# • Класс должен иметь атрибуты «Название», «Объем» и «IBU», которые должны присваиваться инициализатору при создании экземпляра класса;
# • Класс должен иметь метод «Сгонять», который возвращает строку в зависимости от значения «IBU»:
#  - Если «IBU» меньше 10 – «Слабое пиво»;
#  - Если «IBU» меньше 30 – «Среднее пиво»;
#  - В противном случае – «Крепкое пиво»;
# • Класс должен иметь метод «Представление», возвращающий строку в виде «название пива (объем)»;
# • Класс должен иметь метод «Оценка», возвращающий строку в зависимости от значения «IBU»:
#  - Если «IBU» меньше 10 – «Очень сладкое пиво»;
#  - Если «IBU» меньше 30 – «Отличное пиво»; 
#  - В противном случае – «Очень горькое пиво»;

# Нефункциональные требования:
# • Код должен быть простым и читаемым;
# • Использовать имена переменных и функций, соответствующие их функциям;
# • Использовать правильные практики ООП.

class Beer:
    def __init__(self, name, Vol,IBU) -> None:
        self.name = name
        self.Vol = Vol
        self.IBU = IBU
    
    def beer_strength(self):
        if(self.IBU < 10):
            print("Слабое пиво")
        elif(self.IBU < 30):
            print("Среднее пиво")
        else:
            print("Крепкое пиво")
            
    def Performance(self):
        print(self.name + ' (' + str(self.Vol) + ')', sep ='')
        
    def Rating(self):
        if(self.IBU < 10):
            print("Очень сладкое пиво")
        elif(self.IBU < 30):
            print("Отличное пиво")
        else:
            print("Очень горькое пиво")
            
            



# 2) Задача на наследование:
# 1. Цель
# Создание классов для представления сущностей "Барби" и "Кукла Барби" 
# на языке Python с использованием принципов ООП наследования.

# 2. Требования
# 2.1. Необходимо создать два класса: "Барби" (Barbie) и "Кукла Барби" (BarbieDoll).
# 2.2. Класс "Барби" должен содержать информацию о внешнем виде, ментальности и характере Барби.
# 2.3. Класс "Кукла Барби" должен наследовать все свойства класса "Барби" 
# и также содержать информацию о материале, из которого она сделана (пластик, бархат и т.д.),
# о типе производства (массовое или ограниченное), цвете, 
# дополнительных атрибутах и деталях (настроечные глаза, тканевые юбки и т.п.).
# 2.4. Для каждого класса требуется создать методы, которые позволят получать и изменять значения атрибутов.

# 3. Инструкция
# 3.1. Создайте два класса: "Барби" и "Кукла Барби".
# 3.2. В класс "Барби" добавьте атрибуты для представления ее внешнего вида, ментальности и характера.
# 3.3. В класс "Кукла Барби" добавьте атрибуты, такие как материал,
# из которого она сделана, тип производства, цвет и дополнительные атрибуты и детали.
# 3.4. Укажите для каждого класса методы для получения и изменения атрибутов.
# 3.5. Убедитесь, что класс "Кукла Барби" наследует все атрибуты и методы класса "Барби".


class Barbie:
    def __init__(self, appearance, mentality, character) -> None:
        self.appearance = appearance
        self.mentality = mentality
        self.character = character
    #Инфа по атрибутам    
    def appearance_info(self):
        print(self.appearance)
    
    def mentality_info(self):
        print(self.mentality)
    
    def character_info(self):
        print(self.character)
    
    #Изменение атрибутов    
    def appearance_change(self, new_appearance):
        self.appearance = new_appearance
    
    def mentality_change(self, new_mentality):
        self.mentality = new_mentality
    
    def character_change(self, new_character):
        self.character = new_character    
        
class BarbieDoll(Barbie):
    
    def __init__(self, appearance, mentality, character, material, type_of_production, color, other_details) -> None:
        super().__init__(appearance, mentality, character)
        self.material = material
        self.type_of_production = type_of_production
        self.color = color
        self.other_details = other_details
        
    #Инфа по атрибутам    
    def material_info(self):
        print(self.material)
    
    def type_of_production_info(self):
        print(self.type_of_production)
    
    def color_info(self):
        print(self.color)
    
    def other_details_info(self):
        print(self.other_details)
        
    #Изменение атрибутов    
    def material_change(self, new_material):
        self.material = new_material
    
    def type_of_production_change(self, new_type_of_production):
        self.type_of_production = new_type_of_production
    
    def color_change(self, new_color):
        self.color = new_color
    
    def other_details_change(self, new_other_details):
        self.other_details = new_other_details        
        





