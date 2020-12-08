def brute_force(text, pattern): # O(n) time
    # pattern = consonants
    count = maxcount = 0
    start = 0
    res = {}
    for end in range(len(text)):
        if text[end] in pattern: 
            count += 1
        elif text[end] not in pattern or end == len(text)-1:
            maxcount = max(maxcount, count)
            res[maxcount] = start
            count = 0


vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
#print(brute_force('Loremwououmw',consonants))

'''
with open('lorem_ipsum.txt','r') as f:
    for line in f.read().splitlines():
        words = line.split()
        
        for word in words:
            if word != '':
                count, ind  = brute_force(word.lower(), vowels)
                print(word, count, ind)
'''       
    