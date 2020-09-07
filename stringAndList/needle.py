'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        nLen = len(needle)
        #print(nLen)
        if nLen == 0:
            return 0
        
        i = 0
        while i < len(haystack):

            if haystack[i] == needle[0]:
                #print(i, haystack[i:i+nLen])
                if haystack[i:i+nLen] == needle:
                    return i
            i += 1

        return -1

sol = Solution()
print(sol.strStr("mississippi","issip"))
print(sol.strStr("hello","ll"))
