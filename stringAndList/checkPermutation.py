def checkPermutation(a, b): 
    '''
    check if a is permute of b
    O(nlogn) when n is the sum of length a and b 
    Solution 1: check if length equal => sort a and b and compare => O(aloga) and O(blogb), O(n) space
    Solution 2: create a dict and map each character of b with its frequency, iterate through first string then decrement the dict through 2nd string => O(n)
    '''

    # Solution 1:
    print(sorted(a))
    print(sorted(b))
    
    if len(a) != len(b):
        return False

    elif sorted(a) == sorted(b):
        return True
    else:
        return False


print(checkPermutation('abacd', 'dahae'))
print(checkPermutation('abacd', 'adcab'))
print(checkPermutation('abacd', 'adc'))
print(checkPermutation('aba cd', 'ad cab'))

print('SOLUTION 2')

def checkPermutation2(a, b): 
    '''
    check if a is permute of b
    O(nlogn) when n is the sum of length a and b 
    Solution 1: check if length equal => sort a and b and compare => O(aloga) and O(blogb), O(n) space
    Solution 2: create a dict and map each character of b with its frequency, iterate through first string then decrement the dict through 2nd string => O(n) time and space
    '''

    # Solution 2:

    if len(a) != len(b):
        return False

    dictb = {}
    for char in b: 
        if char not in dictb.keys(): 
            dictb[char] = 1 
        else:
            dictb[char] += 1 

    print('1st loop', dictb)

    for char in a:
        if char in dictb.keys(): 
            if dictb[char] > 1: 
                dictb[char] -= 1
            else: 
                del dictb[char]
        else:
            return False

    print('2nd loop', dictb)

    if len(dictb) == 0:
        return True

    else:
        return False 

print(checkPermutation2('abacd', 'dahae'))
print(checkPermutation2('abacd', 'adcab'))
print(checkPermutation2('abacd', 'adc'))
print(checkPermutation2('aba cd', 'ad cab'))

