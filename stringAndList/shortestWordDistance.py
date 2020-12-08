'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = "coding", word2 = "practice"
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:
    def shortestDistance(self, words, word1, word2):
        w1 = float('inf') # latest index of word1
        w2 = float('inf') # latest index of word2
        diff = float('inf')

        for i in range(len(words)):
            if words[i] == word1:
                w1 = i
            elif words[i] == word2:
                w2 = i
            
            diff = min(abs(w1-w2), diff)

        return diff

sol = Solution()
print(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'practice', 'makes'))
print(sol.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'practice', 'coding')) 