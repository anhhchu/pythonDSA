'''
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""
'''

class Solution:
    def largestTimeFromDigits(self, A):
        ''' 
        generate all 4! from A and check valid time and sort
        '''
        A.sort()

        if A == [0, 0, 0, 0]:
            return '00:00'

        s = ''.join([str(num) for num in A])
        allPermute = self.permute(s, '', [])

        if allPermute == []:
            return ''

        allPermute.sort()

        output = allPermute[-1]
        return output[:2] + ':' + output[2:] 
            

    def permute(self, s, prefix, output):
        if len(s) == 0: 
            if prefix not in output and prefix<'2400' and str(prefix)[2:] < '60': 
                output.append(prefix)
            return output
        
        for i in range(len(s)):
            rem = s[:i] + s[i+1:]
            self.permute(rem, prefix + s[i], output)

        return output

sol = Solution()
print(sol.largestTimeFromDigits([2,4,3,0]))
sol = Solution()
print(sol.largestTimeFromDigits([5,5,5,5]))
sol = Solution()
print(sol.largestTimeFromDigits([0,0,0,0]))
sol = Solution()
print(sol.largestTimeFromDigits([0,0,1,0]))
sol = Solution()
print(sol.largestTimeFromDigits([2,4,0,0]))
sol = Solution()
print(sol.largestTimeFromDigits([4,2,4,4]))
sol = Solution()
print(sol.largestTimeFromDigits([1,9,6,0]))
sol = Solution()
print(sol.largestTimeFromDigits([8,8,0,1]))
