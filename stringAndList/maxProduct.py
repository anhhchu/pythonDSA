'''
Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''


class Solution(object):
    def maxProductBruteForce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(N^2) with 2 loops, O(1) space with 2 variables 
        """
        
        result = nums[0]
        
        for i in range(len(nums)):
            accum = 1
            for j in range(i,len(nums)): 
                accum *= nums[j]
                result = max(result, accum)
        
        return result 


    def maxProductDP(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Using Dynamic Programming
        O(N) time using 2 pointers, O(1) space
        """
        # curr = current value
        # 2 pointers 
            # max_so_far = max(curr, curr*max_so_far, curr*min_so_far)
            # min_so_far = min(curr, curr*max_so_far, curr*min_so_far)
        # return max(result, max_so_far)
        
        if len(nums) == 1:
            return nums[0]
        
        curr = result = max_so_far = min_so_far = nums[0]
        
        for curr in nums[1:]:
            
            val1 = curr*max_so_far
            val2 = curr*min_so_far
            max_so_far = max(curr, val1, val2)
            min_so_far = min(curr, val1, val2)
            result = max(result, max_so_far)
        
        return result 

sol = Solution()
testCases = [[2,3,-2,4],[1,2,-3,-4,5,0,6,7,0],[-2,0,-1],[-1],[-4,-3],[3,-1,4],[2,-5,-2,-4,3], [2,-5,3,1,-4,0,-10,2,-8]]
for arr in testCases:
    print(sol.maxProductBruteForce(arr))
    print(sol.maxProductDP(arr))



