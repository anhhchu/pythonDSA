def urlify(string):
    '''
    replace space in string with %20
    copy char of string to list, encounter '', change to '%20', then join list
    -> O(n) space, O(n) time for the iteration 
    '''
    l = []
    for char in string:
        if char == ' ':
            l.append('%20')
        else:
            l.append(char)
    
    print(l)

    string = ''.join(char for char in l)

    return string

print(urlify('geek for geek'))
print(urlify('coding interview '))