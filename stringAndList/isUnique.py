# check if a string contains only unique character

def isUnique(string):
    '''
    O(nlogn) time and O(n) space for sorted algorithm
    O(n) time for the for loop
    '''

    sorted_string = ''.join(sorted(string))
    for i in range(1, len(string)):
        if sorted_string[i] == sorted_string[i-1]:
            return False
    return True


print(isUnique('abcd'))
print(isUnique('abadc'))
print('special char', isUnique('adahlakhgeuworhqep;hgfashgdvoasf;ald'))

def isUniquenew(string):
    '''
    solution with O(n) time and O(n) space 
    '''
    charSet = [None for _ in range(len(string))] # Assume ASCII character set
    for i, char in enumerate(string):
        if char not in charSet:
            charSet[i] = char
        else:
            return False

    return True

print(isUniquenew('abcd'))
print(isUniquenew('asadc'))
print('special char', isUniquenew('adahlakhgeuworhqep;hgfashgdvoasf;ald'))