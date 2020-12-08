'''
Assignment 6: String Algorithms
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


def brute_force(text, pattern): # O(n) time
    count = maxcount = 0
    indexes = []
    start = end = None
    for i, char in enumerate(text):
        #print(i,char)
        if char.lower() in pattern:
            count+= 1
            indexes.append(i)
        if char.lower() not in pattern or i == len(text)-1:
            if count > maxcount:
                start, end = indexes[0], indexes[-1]
                maxcount = max(maxcount, count)
            # reset count and indexes
            count = 0
            indexes = []
    

    if not (start and end): ind = 'not exists'
    elif start == 0 and end == len(text)-1: ind = 'both'
    elif start == 0: ind = 'prefix'
    elif end == len(text)-1: ind = 'suffix'
    else: ind = 'mid'

    return (maxcount, ind)

vowels = set(['a', 'e', 'i', 'o', 'u'])
consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
#print(brute_force('Loremwououmw',consonants))


with open('lorem_ipsum.txt','r') as f:
    for line in f.read().splitlines():
        words = line.split()
        
        for word in words:
            if word != '':
                print(word)
                #count_vowels, ind_vowels  = brute_force(word, vowels)
                #print(word, count_vowels, ind_vowels)
                count_consonants, ind_consonants  = brute_force(word, consonants)
                print(word, count_consonants, ind_consonants)
      
    
'''
def stringAlgo(file):
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    consonants = set(['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'])
    
    max_vowel_count = max_vowel_prefix = max_vowel_suffix = max_cons_count = max_cons_prefix = max_cons_suffix = 0
    res_max_vowel = res_max_vowel_prefix = res_max_vowel_suffix = res_max_cons_count = res_max_cons_prefix = res_ax_cons_suffix = []
    

    with open(file,'r') as f:
        for line in f.read().splitlines():
            words = line.split()
            for word in words:
                print(word)
                if word != '':
                    #count_vowels, ind_vowels = brute_force(word, vowels)
                    count_consonants, ind_consonants = brute_force(word, consonants)
                    print(word, count_consonants, ind_consonants)
                    #if count_vowels > max_vowel_count: 
                        


stringAlgo('lorem_ipsum.txt')
'''