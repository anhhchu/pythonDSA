'''
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 https://leetcode.com/problems/repeated-substring-pattern/

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

'''


class Solution(object):
    def repeatedSubstringPattern_regex(self, s):
        """
        :type s: str
        :rtype: bool
        complexity O(N^2) time, O(1) space
        """
        import re
        pattern = re.compile(r'^(.+)\1+$')
        output = pattern.match(s)
        #print(output)
        #print(pattern)
        return output

    def repeatedSubstringPattern_concatenate(self, s):
        """
        complexity O(N^2) as for each element of s, check for its presence in s+s
        """
        return s in (s+s)[1:-1]


    def repeatedSubstringPattern_RabinKarp(self, s):   
        '''
        Deal with base cases: n <= 2.

        Iterate from sqrt{n} to1.

        For each divisor n % i == 0:

            Compute paired divisor n / i.

            Use Rabin-Karp to check substrings of the lengths l = i and l = n / i:

            Take as a reference hash first_hash the hash of the first substring of length l.

            Jump along the string with a step of length l while the hash of the current substring is equal to first_hash.

            If the hashes of all substrings along the way are equal, the input string consists of repeated patterns of length l. Return True.

        time: O(n*sqrt(n)). O(sqrt(n)) for divisor computation, O(n) for each element verification
        space: O(sqrtN) for hash copy
        '''
        # base case
        n = len(s)

        if n < 2:
            return False

        elif n == 2:
            return s[0] == s[-1]
        
        for i in range(int(n**0.5), 0, -1):
            if n%i == 0:
                divisors = [i]
                if i != 1:
                    divisors.append(n//i)
                #print(i, divisors)
                for l in divisors:
                    #print(l)
                    firstSub = currSub = hash(s[:l])
                    start = l
                    while start != n and firstSub == currSub: 
                        currSub = hash(s[start:start+l])
                        start += l

                    if start == n and firstSub == currSub: 
                        return True

        return False
        


sol = Solution()

print('***CONCATENATE')
print(sol.repeatedSubstringPattern_concatenate("abcabc"))  
print(sol.repeatedSubstringPattern_concatenate("abcabcabcabc"))  
print(sol.repeatedSubstringPattern_concatenate("aba"))  
print(sol.repeatedSubstringPattern_concatenate("aa"))  

print('***RABIN KARP - MULTIPLE PATTERN SEARCH')
print(sol.repeatedSubstringPattern_RabinKarp("aa"))  
print(sol.repeatedSubstringPattern_RabinKarp("abcabc"))  
print(sol.repeatedSubstringPattern_RabinKarp("abcabcabcabc"))  
print(sol.repeatedSubstringPattern_RabinKarp("ababab"))  





