from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, flavor=None, calories=None):
        super().__init__(name, calories)
        self.__flavor = flavor

    @property    
    def flavor(self):
        if self.__flavor is not None:
            return self.__flavor
        else:
            raise Exception("Can't get a value which is not initialized")

    @flavor.setter
    def set_flavor(self, flavor):
        self.__flavor = flavor
    # overriding the is_delicious method from task_11.py file
    def is_delicious(self):
        if self.__flavor is not None:
            if self.__flavor == "black licorice":
                return False
            return True
        else:
            raise Exception("You can't call this method unless you initialize the necessary attributes")
 


# JellyBean1 = JellyBean("jelly bean", 'black licorice')
# print(JellyBean1.get_calories())
# print(JellyBean1.get_name())
# print(JellyBean1.is_delicious())
# JellyBean1.set_flavor("caramel")
# print(JellyBean1.get_flavor())
