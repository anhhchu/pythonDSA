class Solution:
    def removeDuplicates(self, nums):
        j = len(nums)
        i = 1
        while i < j:
            print(nums)
            if nums[i-1] == nums[i]:
                nums[i] = nums[i+1]
                j -= 1
                #i += 1
            else:
                i += 1
        return j + 1

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)