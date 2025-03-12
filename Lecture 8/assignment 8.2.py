import string

def is_palindrome(text):
    punct = str.maketrans('', '', string.punctuation + ' ')
    x = text.translate(punct).lower()
    return x == x[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")