from functools import reduce

def multiply_numbers(*args):
    if args:
        new_list = []
        for i in args:
            if isinstance(i, str):
                digits = [int(ch) for ch in i if ch.isdigit()]
                if digits:
                    new_list.extend(digits)
            elif isinstance(i, (float)):
                lst = [int(j) for j in str(i) if j.isdigit()]
                new_list.extend(lst)
            elif isinstance(i, (int)):
                new_list.append(i)
            elif isinstance(i, (tuple, list, set)):
                digits = [int(num) for num in i if isinstance(num, (int, float, str)) and str(num).isdigit()]
                if digits:
                    new_list.extend(digits)
        if new_list:
            return reduce(lambda x,y: x*y, new_list)
    return None

# print(multiply_numbers()) # => None
# print(multiply_numbers('ss')) # => None
# print(multiply_numbers('1234')) # => 24
# print(multiply_numbers('sssdd34')) # => 12
# print(multiply_numbers(2.3)) # => 6
# print(multiply_numbers([5, 6, 4])) # => 120