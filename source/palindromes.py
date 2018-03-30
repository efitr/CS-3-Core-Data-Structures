#!python

import string
from math import ceil
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase

def clean(palindrome):
    palindrome = palindrome.lower()
    palindrome = palindrome.replace(" ", "")
    #Add punctuation remover
    return palindrome

def is_palindrome(text):
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_recursive(text, left=None, right=None)
    # return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    #from right to left it is the same

    text = clean(text)
    if text == '':
        return True

    if len(text) == 1:
        return True

    middle_position = ceil(len(text)/2)
    position = 0
    last_position = len(text)-1

    while text[position] == text[last_position]:
        if position == middle_position:
            return True
        position += 1
        last_position -= 1
    return False



def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    #if left is None and right is None:


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
