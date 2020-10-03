'''
compress the string duplications
aaabcccdd -> a3b1c2d2
'''

def stringCompression(string):
    '''
    O(n) time, O(n) space
    '''
    i, j = 0, 1
    if len(set(string)) == len(string):
        return string
    while j < len(string):
        if string[i] == string[j]:
            if j == len(string)-1:
                #print(i,j)
                string = string[:i+1]+str(j-i+1)
                break
            else: j+=1
        else:
            string = string[:i+1]+str(j-i)+string[j:]
            i += 2
            j = i+1
        #print(len(string))

    return string

print(stringCompression('aaabcccdd'))
print(stringCompression('a'))
print(stringCompression('ab'))
print(stringCompression('aa'))
print(stringCompression('aabccdeeaa'))
print(stringCompression('aba'))

    
    
