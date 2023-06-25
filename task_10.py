"""
Разработайте функцию count_words(string), которая будет возвращать словарь со
статистикой частоты употребления входящих в неё слов.
"""
import re

def count_words(string):
    counter_for_each_word = []
    counter = 0
    if string is not None and isinstance(string, str):

        string = (re.sub(r'[^\w\s]', '', string.lower()).split())
    set_string = set(string)
    for i in set_string:
        counter_for_each_word.append(string.count(i))
    return dict(zip(set_string, counter_for_each_word))
         
        

       
# print(count_words("A man, a plan, a canal -- Panama"), # => {"a": 3, "man": 1,
# # "canal": 1, "panama": 1, "plan": 1}
# count_words("Doo bee doo bee doo")) # => {"doo": 3, "bee": 2}