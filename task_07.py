
def anagrams(word, words):     
    return list(filter(lambda x: sorted(word) == sorted(x), words))

def combine_anagrams(words_array):
    if words_array is not None:
        anagram_array = []
        words_array = [i.lower() for i in words_array]
        iterable = iter(words_array)
        for _ in range(len(words_array)):
            current_word = words_array[0]
            lst = anagrams(current_word, words_array)
            anagram_array.append(lst)
            words_array = list(filter(lambda w: w not in lst, words_array))
            try:
                current_word = words_array[0]
            except:                
                return anagram_array # p.s. на вывод вернется список немного в другом порядке(есть ли разница порядка вывода подсписков?)
# print(combine_anagrams(["cars", "for", "potatoes", "racs", "four", "scar",
#  "creams", "scream"])) # => [ ["cars", "racs", "scar"], ["four"], ["for"],
# # ["potatoes"], ["creams", "scream"] ] 
           