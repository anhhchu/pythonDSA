class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        use 2 pointers: O(N) time, O(1) space
        """
        # curr is the current value
        # cumS = max(cumS, curr)
        # maxS = max(curr, cumS, maxS)
        if len(nums) == 0:
            return nums[0]
        
        curr = cumS = maxS = nums[0]
        for curr in nums[1:]:
            S = curr + cumS
            cumS = max(S, curr)
            maxS = max(curr, cumS, maxS)
            
        return maxS

testCases = [[-2,1,-3,4,-1,2,1,-5,4],[-2,1,-3,0,-1,2,1,-5,4]]
sol = Solution()
for test in testCases:
    print(sol.maxSubArray(test))