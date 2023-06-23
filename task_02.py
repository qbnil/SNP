def coincidence(lst=None, rng=None):
    if lst is not None and rng is not None:
        same_values = []   
        for i in lst:
            if not isinstance(i, (str, type(None))):
                if int(i) in rng:
                    same_values.append(i)
        return same_values
    else:
        empty_list = []
        return empty_list
# print(coincidence([1, 2, 3, 4, 5], range(3, 6))) # => [3, 4, 5]
# print(coincidence()) # => []
# print(coincidence([None, 1, 'foo', 4, 2, 2.5], range(1, 4)))