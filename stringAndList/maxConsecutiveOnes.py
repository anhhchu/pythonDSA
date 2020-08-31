class Solution:
    def findMaxConsecutiveOnes(self, nums):
        '''
        log(N) 
        '''
        maxCount, count = 0, 0

        # edge cases
        if len(nums) == 0: 
            return maxCount

        elif len(nums) == 1:
            if nums[0] == 1:
                maxCount += 1
            return maxCount

        else: 
            for val in nums:
                if val == 1:
                    count+=1
                else:
                    if maxCount < count:
                        maxCount = count
                    count = 0 
            if maxCount < count:
                maxCount = count
        
        return maxCount


sol = Solution()
nums = [1]
print(sol.findMaxConsecutiveOnes(nums))

nums = [0]
print(sol.findMaxConsecutiveOnes(nums))
        
nums = [1,0,1,1,0,1]
print(sol.findMaxConsecutiveOnes(nums))
        
nums = [1,1,0,1,1,1]
print(sol.findMaxConsecutiveOnes(nums))