"""
Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
принимающим на вход name и calories (не обязательные параметры), а также двумя
методами is_healthy (возвращает true при условии калорийности десерта менее
200) и is_delicious (возвращает true для всех десертов).
"""

class Dessert:
    def __init__(self, name=None, calories=None):
        self.__calories = calories
        self.__name = name

    def is_healthy(self):
        return True if self.__calories is not None and self.__calories<200 else False if self.__calories is not None else Exception("Attribute must be initialized before calling this method")

    def is_delicious(self):
        return True

    @property
    def calories(self):
        if self.__calories is not None:
            return self.__calories
        else:
            raise Exception("You didn't initialize the calories for the dessert object")
    @property 
    def name(self):
        if self.__name is not None:
            return self.__name 
        else:
            raise Exception("Attribute must be initialized before calling this method")

    @calories.setter
    def calories(self, calories):
        if type(calories) is int:
            self.__calories = calories
        else:
            raise Exception("Calories number has to be an integer type")
    
    @name.setter
    def name(self, name):
        self.__name = name
    



dessert1  = Dessert("чизкейк", 234)
dessert1.calories = 123
print(dessert1.calories)
