import re
def is_palindrome(txt):
    if txt is not None and type(txt) is not int:
        squashed_string = re.sub(r'[^\w\s]', '', txt.lower()).replace(" ", "")
        # print(squashed_string[::-1])
        return squashed_string==squashed_string[::-1]
    else:
        return False

# print(is_palindrome("A man, a plan, a canal -- Panama"))
# print(is_palindrome("Madam, I'm Adam!"))
# print(is_palindrome("Abracadabra"))
# print(is_palindrome(None))