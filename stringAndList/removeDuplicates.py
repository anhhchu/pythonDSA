class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for n in nums:
            print(i, n, nums) 
            if n != nums[i]:
                nums[i+1] = n
                i += 1
        return i+1

nums = [0,0,1,1,1,2,2,3,3,4]
sol = Solution()
print(sol.removeDuplicates(nums))
print(nums)