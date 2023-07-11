from task_11 import Dessert

class JellyBean(Dessert):
    def __init__(self, name=None, flavor=None, calories=None):
        super().__init__(name, calories)
        self.__flavor = flavor

        
    def get_flavor(self):
        if self.__flavor is not None:
            return self.__flavor
        else:
            raise Exception("Can't get a value which is not initialized")
    def set_flavor(self, flavor):
        if self.__flavor is not None:
            self.__flavor = flavor
        else:
            raise Exception("Calling a method on a non-existing attribute of a class, initialize it")
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
