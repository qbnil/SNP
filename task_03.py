def max_odd(lst):
    if lst is not None:
        new_list = []
        for i in lst:
            if type(i) == list or type(i) == set or type(i) == tuple:
                for j in i:
                    if isinstance(j, (int, float)):
                        new_list.append(j)          
            if isinstance(i, (int, float)):
                new_list.append(i)
        lst2 = list(filter(lambda n: n%2==1, new_list))
        # print(lst2)
        return max(map(int, lst2)) if len(lst2)>=1 else None
        

# print(max_odd([1, 2, 3, 4, 4]), # => 3
# max_odd([21.0, 2, 3, 4, 4]), # => 21
# max_odd(['ololo', 2, 3, 4, [1, 2], None]), # => 3
# max_odd(['ololo', 'fufufu']), # => None
# max_odd([2, 2, 4]), # => None
# max_odd(['ololo', 2, 3, 4, [1, 5], None])) # => 3
# print(max_odd([[2,5,6,6,9,1], (2,6,2,3), {2,5,2,6,1,7}]))