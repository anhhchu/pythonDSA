'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        freq = n//3 + 1
        
        seen = {} # space O(n)
        result = []
        while nums:  # loop through O(n) time
            num = nums.pop()  # pop element from nums and add to seen to save space
            if num in seen: 
                seen[num] += 1
            else:
                seen[num] = 1
            
            if seen[num] >= freq and num not in result:
                result.append(num)
        
        print(seen)      
        return result
        
        
        
        
         
        