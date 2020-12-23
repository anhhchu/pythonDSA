'''
String Algorithms
You have been provided with the following string matching algorithms: Boyer_Moore.py, Brute_force.py, KMP_matcher.py, and Rabin_Karp.py. Using any of these algorithms, I want you to find the word(s) that have:
1. Longest Continual Substring of:
Vowels
Consonants
2. Longest Continual Prefix of:
Vowels
Consonants
3. Longest Continual Suffix of:
Vowels 
Consonants
Example: ["Hello", "World", "Face","Asthma", "Spring", "Because", "Thorough", "Sequoia" ]. In this list of strings, "Sequoia" has the longest substring of consecutive vowels. "Asthma" has the longest substring of consecutive consonants. "Asthma" Also has the longest prefix of consecutive vowels. "Spring" has the longest prefix of consecutive consonants. "World" has the longest suffix of consecutive consonants and "Sequoia" has the longest suffix of consecutive vowels. Your word file is going to be a long excerpt from "Lorem Ipsum" text found in lore_ipsum.txt. If there are multiple words that tie in any criteria, return ALL words that tie. You can assume that the only characters in the file will be standard English letters, no numbers, special characters, or characters with diacritic marks.


'''

vowels = set(['a','e','i','u','o','y'])
consonants = set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z'])
def brute_force(text, pattern):
    '''
    for each character in text, check if character in pattern
    increment the prefix, suffix and max count accordingly
    return:
    - maxcount, prefix and suffix count

    # text = 'ipsum'
    # pattern = consonants
    # return count = 2, prefix = 0, suffix = 1
    '''
    text = text.lower()
    i = 0
    n = len(text)
    count = maxcount = 0
    #start = None
    prefix = suffix = 0

    # first char in text, get count for prefix
    if text[0] in pattern: 
        for char in text:
            if char in pattern:
                prefix+=1
            else:
                break
    
    # last char in text, get count for suffix
    if text[-1] in pattern: 
        for char in reversed(text):
            if char in pattern:
                suffix+=1
            else:
                break
    
    # use 2 pointers to get count for longest substring that contains the pattern
    while i<n:
        j = i
        #print('start', i,j, text[j])
        if text[j] not in pattern:
            i += 1
        else: 
            while j<n and text[j] in pattern: 
                count += 1
                j += 1
            # j = u
            if count >= maxcount:
                maxcount = count
                #start = i
            count = 0
            #print(j,count,maxcount, start)
            i = j+1

    return (maxcount, prefix, suffix)

#print(brute_force('Praesent', consonants))


def main():
    from collections import defaultdict
    s = []
    with open('lorem_ipsum.txt','r') as f:
        for line in f.read().splitlines():
            words = line.split()
            for word in words:
                if word != ' ':
                    s += word.split(' ')
                    #subset = word.split(' ')

    #maxcons, maxvows = 0, 0
    consAns, prefCAns, sufCAns, vowsAns, prefVAns, sufVAns = defaultdict(set), defaultdict(set),defaultdict(set),defaultdict(set),defaultdict(set),defaultdict(set)

    for word in s:
        #print(word)
        word = ''.join(e for e in word if e.isalnum())
        countC, prefixC, suffixC = brute_force(word, consonants)
        countV, prefixV, suffixV = brute_force(word, vowels)
        
        consAns[countC].add(word)
        prefCAns[prefixC].add(word)
        sufCAns[suffixC].add(word)

        vowsAns[countV].add(word)
        prefVAns[prefixV].add(word)
        sufVAns[suffixV].add(word)

        # consAns = {3:set(['hendrerit', 'ultrices', 'ultricies', 'porttitor']), 1:set(), 2:set()}
        
 
    return [consAns[max(consAns)], prefCAns[max(prefCAns)], sufCAns[max(sufCAns)], vowsAns[max(vowsAns)], prefVAns[max(prefVAns)], sufVAns[max(sufVAns)]]

ans = main()
print("Longest Continual Consonants", ans[0])
print("Longest Continual Prefix consonants", ans[1])
print("Longest Continual Suffix Consonants", ans[2])
print("Longest Continual Vowels", ans[3])
print("Longest Continual Prefix Vowels", ans[4])
print("Longest Continual Suffix Vowels", ans[5])
