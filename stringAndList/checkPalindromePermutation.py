def checkPalindrome(string):
    '''
    check if a permutation of a string is palindrome
    solution O(n) time, O(n) space
    use a hashtable(dictionary) to keep track of the count of each character. 
    if string has even length, number of characters need to be even. if string has odd length, only 1 character appears 1
    REMEMBER SPECIAL CHARACTERS
    '''
    dictP = {}
    # only add alphanumeric 
    for char in string:
        if char.isalnum(): 
            if char not in dictP: 
                dictP[char] = 1
            else: 
                dictP[char] += 1

    print(dictP)

    # count odd
    countOdd = 0
    for freq in dictP.values():
        # a character appears odd numbers of time  
        if freq % 2 != 0 and freq > 1:
             return False
        
        elif freq == 1:
            countOdd += 1

    if countOdd > 1: 
        return False

    elif len(string) % 2 == 0 and countOdd == 0: 
        return True

    elif len(string) % 2 != 0 and countOdd == 1: 
        return True
    
    else: 
        return False


print(checkPalindrome('tacotac'))

print(checkPalindrome('a'))

print(checkPalindrome('ttttaaaaccco'))

print(checkPalindrome('ttttaaaacccco'))
