'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 10
'''

class Solution:
    def rotateArrayReverse(self, nums,k):
        '''using Reverse'''
        # nums = [1,2,3,4,5,6,7]
        # reverse: 7,6,5,4,3,2,1
        # reverse 1st and 2nd half: 5,6,7,1,2,3,4
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start+=1
                end -=1
        n = len(nums)
        k %= n
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)  

    def rotateArrayExtraSpace(self,nums,k):
        n = len(nums)
        k %= n
        i = n-k
        nums[:] = nums[i:] + nums[:i] 

sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotateArrayReverse(nums,3)
nums = [1,2,3,4,5,6,7]
sol.rotateArrayExtraSpace(nums,3)
print(nums)
