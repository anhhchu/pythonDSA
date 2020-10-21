'''
Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2
'''

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Using dynamic programming
        O(n) time, O(n) space
        """
        # create a frequency hash
        seen = {}
        for num in nums:
            if num not in seen: seen[num] = 1
            else: seen[num] += 1

        # construct 
        count = 0
        if k == 0:
            for num, values in seen.items():
                if values >= 2:
                    count += 1
            return count
        
        else:
            for num in seen.keys():
                diff = num + k
                if diff in seen:
                    count += 1
            return count
        
sol = Solution()

print(sol.findPairs([3,1,4,1,5], 2))
        