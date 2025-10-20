def lvl1(text :str, method :str):
    if method == 'upper':
        return str.upper(text)
    if method == 'lower':
        return str.lower(text)
    return str.capitalize(text)
def lvl2(text :str, method: str, what :str, onwhat :str):
    if method == 'find':
        return text.find(what)
    if method == 'replace':
        return text.replace(what, onwhat)
    if method == 'count':
        return text.count(what)
    if method == 'index':
        return text.index(what)
def lvl3(text :str, method: str, bywhat :str):
    if method == 'split':
        return text.split(bywhat)
    return ''.join(text.split(bywhat))
def lvl4(text: str, method :str, what :list):
    if method == 'isdigit':
        return text.isdigit()
    if method == 'isalpha':
        return text.isalpha()
    if method == 'strip':
        return text.strip(''.join(what))
    return text.format(what)
print('Choose lvl of dungeon(1, 2, 3, 4 or 5): ')
lvl = int(input())
if lvl == 1:
    print('Enter your text:')
    text = str(input())
    print('Choose the method:\n1)upper - Converts all text letters to  uppercase\n2)lower - Converts all text letters to lowercase\n3)capitalize - Sets the letter case according to grammar rules')
    method = str(input())
    print('Your text:')
    print(lvl1(text, method))
if lvl == 2:
    onwhat = ''
    print('Enter your text:')
    text = str(input())
    print('Choose the method:\n' \
    '1)find - searches for the index of the first occurrence of an element in a string\n' \
    '2)replace - replaces a specific substring with the provided value\n' \
    '3)count - counts the number of occurrences of a substring\n' \
    '4)index - finds the index of the first element of the first occurrence of a substring')
    method = str(input())
    print('Enter the substring you want to work with:')
    what = str(input())
    if method == 'replace':
        print('Enter the substring you want to replace the original one with:')
        onwhat = str(input())
    print('Your text:')
    print(lvl2(text, method, what, onwhat))
if lvl == 3:
    print('Enter your text:')
    text = str(input())
    print('Choose the method:\n' \
    '1)split - Return a list of the words in the string, using given substring as the delimiter string\n' \
    '2)join - Return a string which is the concatenation of the strings of given')
    method = str(input())
    print('What element would you like to split this string up?')
    bywhat = str(input())
    print('Your text:')
    print(lvl3(text, method, bywhat))
if lvl == 4:
    print('Enter your text:')
    text = str(input())
    print('Choose the method:\n' \
    '1)isdigit - Return True if all characters in the string are digits and there is at least one character, False otherwise\n' \
    '2)isalpha - Return True if all characters in the string are alphabetic and there is at least one character, False otherwise.\n' \
    '3)strip - Return a copy of the string with the leading and trailing characters removed\n' \
    '4)format - Perform a string formatting operation. The string on which this method is called can contain literal text or replacement fields delimited by braces {}'
    '(please enter like : 123 {0[0]} 123 {0[1]} 123 {0[2]}  ....)')
    method = str(input())
    if method == 'isdigit' or method == 'isalpha':
        print('What you want to include or remove?')
        what = str(input()).split()
    else:
        what = []
    print('Your text:')
    print(lvl4(text, method , what))

if lvl == 5:
    s = 'pYtHon;is;AWESome;'
    print('The original line:')
    s = s.replace(';',' ')
    s=s.capitalize()
    s=s.strip('')
    print('Final line:')
    print(s)