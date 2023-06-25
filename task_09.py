"""
Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
переданных словаря, значениями ключей в которых являются числа, и вернет
новый словарь, полученный по следующим правилам:

• приоритетными являются ключи того словаря, сумма значений ключей
которого больше (если суммы значений ключей будут равны, то второй
словарь считается более приоритетным)
• ключи со значениями меньше 10 не должны попасть в финальный
словарь
• получившийся словарь должен вернуться упорядоченным по значениям
ключей в порядке возрастания.

"""

def connect_dicts(dict1, dict2):
    if dict1 is not None and dict2 is not None:
        
        filtered_dict1 = {key: val for key, val in dict1.items() if isinstance(val, int) and val >= 10}
        filtered_dict2 = {key: val for key, val in dict2.items() if isinstance(val, int) and val >= 10}

        sum1 = sum(val for val in dict1.values() if isinstance(val, int))
        sum2 = sum(val for val in dict2.values() if isinstance(val, int))

        priority_dict = filtered_dict1 if sum1 > sum2 else filtered_dict2
        if priority_dict == filtered_dict1:
            for key, value in filtered_dict2.items():
                if key not in priority_dict:
                    priority_dict[key] = value
        else:
            for key, value in filtered_dict1.items():
                if key not in priority_dict:
                    priority_dict[key] = value
        resulting_dict = dict(sorted(priority_dict.items(), key=lambda x: x[1]))

        return resulting_dict
            



# print(connect_dicts({ "a": 2, "b": 12 }, { "c": 11, "e": 5 }), # =>
# # { "c": 11, "b": 12 }
# connect_dicts({ "a": 13, "b": 9, "d": 11 }, { "c": 12, "a": 15 }), # =>
# # { d: 11, "c": 12, "a": 13 }
# connect_dicts({ "a": 14, "b": 12 }, { "c": 11, "a": 15 })) # =>
# # { "c": 11, "b": 12, "a": 15 })