class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """

        import operator
        seen = {} 
        banned = set(banned) # O(M) where M is len of banned, set makes easier to check if an item exists
        
        clean_paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph]) # O(N) where N i number of characters
        print(clean_paragraph)  
        
        words = clean_paragraph.split() 
        for w in words:
            if w not in banned:
                if w not in seen:
                    seen[w] = 1
                seen[w] += 1
                
        print(seen)
        
        return max(seen.items(), key=operator.itemgetter(1))[0]


sol = Solution()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol.mostCommonWord(paragraph,banned))
