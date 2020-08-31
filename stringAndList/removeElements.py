class Solution:
    def removeElement(self, nums, val):
        ''' 
        O(n) time, O(1) space
        '''
        j = len(nums)-1
        i = 0
        while i <= j:
            #print((i,nums[i]),(j, nums[j]))
            print(nums)
            if nums[i] == val:
                nums[i] = nums[j]
                nums.pop()
                j -= 1
            else: 
                i += 1

        return len(nums)

sol = Solution()
nums = [0,1,2,2,3,0,4,2]
print(sol.removeElement(nums, 2))
print(nums)