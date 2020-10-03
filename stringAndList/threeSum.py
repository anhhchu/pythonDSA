class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        2 pointers approach: 
            perform two sum on remaining array takes O(n)
            for each element in array, perform two sum => O(n^2)
            sort array takes O(nlogn) 
            Time: O(n^2), space O(n) for the sort

        """
        # check edge case for nums
        # sort the array first 
        # loop for each val of nums, perform two sum II on the remaining array
        output = []  
        if len(nums) < 3: 
            return output
        elif len(nums) == 3:
            s = 0
            for val in nums: s+=val
            if s == 0: 
                return [nums]
            else: 
                return output
        
        # len(nums) > 3    
        nums.sort() # O(nlogn) time, O(n) space

        for i in range(len(nums)): 
            if nums[i] > 0:
                break
            if i == 0 or nums[i-1] != nums[i]:
                self.twoSum(nums, i, output)
            
        return output

        
    def twoSum(self, nums, i, output):
        '''
        2 sum of a sorted array
        2 pointers approach: O(n)
        '''
        l, r = i + 1, len(nums)-1
        while l < r:
            currS = nums[i] + nums[l] + nums[r]
            if currS == 0:
                output.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
            elif currS > 0:
                r -= 1
            elif currS < 0:
                l += 1
            
testCases = [[-1,0,1,2,-1,-4],[-1,0,1,2,-1,0,0],[-1,0,1,2,-1,-1,2,0,0],[0],[],[-1,0,1],[-2,0,1,1,2],[-1,0,1,2,-1,-4,-2,-3,3,0,4]]
sol = Solution()
for arr in testCases:
    print(sol.threeSum(arr))


