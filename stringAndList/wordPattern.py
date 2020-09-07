'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters that may be separated by a single space.
'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strL = str.split(' ')
        if len(strL) != len(pattern):
            return False

        bucket = {}
        for i, char in enumerate(pattern):
            if char not in bucket:
                if strL[i] not in bucket.values():
                    bucket[char] = strL[i]
                else:
                    return False
            else:
                if bucket[char] != strL[i]:
                    return False
        
        return True

sol = Solution()
print(sol.wordPattern("abba", "dog cat cat dog"))
print(sol.wordPattern("abba", "dog cat cat fish"))
print(sol.wordPattern("abba", "dog dog dog dog"))
print(sol.wordPattern("aaaa", "dog cat cat dog"))
