def sort_list(lst):
    if lst is not None and len(lst)>=1:
        lst = list(map(lambda n: max(lst) if n == min(lst) else min(lst) if n == max(lst) else n, lst))
        lst.append(lst[lst.index(min(lst))])
        return lst
    return []
# print(sort_list([]), # => []
# sort_list([2, 4, 6, 8]), # => [8, 4, 6, 2, 2]
# sort_list([1]), # => [1, 1]
# sort_list([1, 2, 1, 3]), sep='\n') # => [3, 2, 3, 1, 1]