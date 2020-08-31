def isPalindrome(string):
    '''
    check if a string is palindrome
    1. if string length <= 1 then False
    2. copy string to list with space remove 
    3. divide list by half
    * if length%2 == 0 -> by half
    * if length %2 != 0 => remove middle element
    4. reverse 2nd half of list
    5. compare 2 list
    O(n) time, O(n) space
    '''
    if len(string) <= 1:
        return False
    
    # copy string to list, ignore special characters and whitespace 
    l = []
    for char in string: 
        if char.isalnum():
            l.append(char)
    print(l)
    
    if len(l) <= 1: 
        return False

    # len(l) >=2, compare value of the end of the list to value at the beginning of the list
    mid = len(l)//2
    i = 0
    j = len(l)-1

    if len(l) % 2 == 0: # len(l) is even 
        while i < mid and j >= mid:  
            if l[i] != l[j]:
                return False
            else:
                i += 1
                j -= 1
        return True

    elif len(l) % 2 != 0:
        while i < mid and j >= mid+1: 
            if l[i] != l[j]:
                return False
            else:
                i += 1
                j -= 1  
        return True


print(isPalindrome('abcd'))
print(isPalindrome('taco cat'))
print(isPalindrome('tacocat'))