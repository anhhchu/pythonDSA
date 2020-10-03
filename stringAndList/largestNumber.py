'''
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.
'''

class Solution(object):
    def largestNumberByDigit(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        O(n) time, O(1) space
        """
        # split num digit by digit 
        # sort the digit descending using counting sort
        count = [0]*10
        for num in nums: # O(n)
            while num >= 10:
                di = num%10
                num = num//10
                count[di] += 1
            count[num] += 1  
        
        output = ''
        
        for d in range(9,-1,-1): # start from end of count # O(1) only 10 slots 
            #print(d,count[d])
            output += str(d)*count[d]
            
        return output

    def largestNumber(self,nums):
        pass

    def test(self, nums, result):
        assert self.largestNumber(nums) == result
 