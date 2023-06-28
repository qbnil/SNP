"""
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""

class Dessert:
    def __init__(self, name, calories=None):
        self.__calories = calories
        self.__name = name

    def is_healthy(self):
        return True if self.__calories is not None and self.__calories<200 else False

    def is_delicious(self):
        return True

    def get_calories(self):
        if self.__calories is not None:
            return self.__calories
        else:
            raise Exception("You didn't initialize the calories for the dessert object")
    
    def get_name(self):
        return self.__name 


    def set_calories(self, calories):
        self.__calories = calories

    def set_name(self, name):
        self.__name = name



# dessert1  = Dessert("чизкейк", 350)
