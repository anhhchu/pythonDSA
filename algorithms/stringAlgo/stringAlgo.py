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


class Solution:
    def brute_force(text, pattern):
    l1 = len(text)      # The text which is to be checked for the existence of the pattern
    l2 = len(pattern)   # The pattern to be determined in the text
    i= 0
    j=0          
 # looping variables are set to 0

    flag = False        # If the pattern doesn't appear at all, then set this to false and execute the last if statement
    while i < l1:       # iterating from the 0th index of text
        j = 0
        count = 0       # Count stores the length upto which the pattern and the text have matched
        while j < l2:
            if i+j<l1 and text[i+j] == pattern[j]:  # statement to check if a match has occoured or not
                count += 1                          # if the statement evaluates to true, then update count
            j += 1
        if count == l2:                             # if total number of successful matches is equal to count of the array
            print("\nPattern occours at index",i)   # print the starting index of the successful match
            flag = True                             # Even if the matching occours once, set this flag to True
        i += 1
    

    def stringAlgo(self):
        vowels = set(['A', 'E', 'I', 'O', 'U'])
        consonants = set(['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'Y'])
        print(vowels, consonants)
        with open('lorem_ipsum.txt','r') as f:
            for line in f.read().splitlines():
                words = line.split(' ')
                for word in words:

        




