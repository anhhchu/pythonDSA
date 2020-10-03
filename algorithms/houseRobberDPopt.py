class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        use pointer, no additional space, 1 pass -> O(N)
        """
        if len(nums) == 0:
            return 0
        
        prevS = currS = 0
        
        for num in nums:
            temp = currS
            currS = max(prevS + num, currS)
            prevS = temp
             
        return currS

sol = Solution()
print(sol.rob([2,1,1,2]))
print(sol.rob([2,7,9,3,1,5,0,4,8]))