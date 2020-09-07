'''
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
'''

# USE HASH TABLE
class Solution(object): 
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        keep value and index of each element in a dictionary 
        if value is seen in the dictionary, check current index compared to index of value in dictionary
        if current idx - value idx > k -> update index of the value in dict
        O(n) space, O(n) time, retrieve value from dictionary takes O(1)

        """
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k: 
                return True
            else: seen[n] = i #update value of current value in seen as index already exceeds k
            #print(seen)

        return False

    def Test(self, nums, k, expected):
        output = self.containsNearbyDuplicate(nums, k)
        if output == expected:
            return 'Pass'
        return 'Fail'


sol = Solution()
print(sol.Test([1,2,3,1,2,3], 2, False))
print(sol.Test([1,0,1,1], 1, True))
print(sol.Test([2,2], 2, True))







