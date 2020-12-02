from collections import Counter
s = "cbacdcbc"

class Solution:
    def removeDuplicate(self,s):
        last_occurred = {c:i for i, c in enumerate(s)}
        stack = []
        


sol = Solution()
sol.removeDuplicate(s)
