'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
 

Constraints:

0 <= nums.length <= 100
0 <= nums[i] <= 400
'''

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        use O(N) space to remember , O(N^2) time
        """
        
        if len(nums) <= 3:
            return self.helper(nums)
        else:
            #print('go to main')
            
            seen = {}
            seen[len(nums)-1] = self.helper(nums[-1:])
            seen[len(nums)-2] = self.helper(nums[len(nums)-2:])
            seen[len(nums)-3] = self.helper(nums[len(nums)-3:])

            total = max(seen[len(nums)-1],max(seen[len(nums)-2],seen[len(nums)-3]))
            
            i = len(nums) - 4
            while i >=0:
                #print(i)
                val = nums[i]
                for j in range(i+2, len(nums)-1):
                    if i in seen: 
                        seen[i] = max(val+seen[j], seen[i])
                    seen[i] = val + seen[j]
                total = max(total, seen[i])
                
                i -= 1
                    
            print(seen)
            #print(total)
            return total

    def helper(self, nums):
        total = 0
        if len(nums) == 0: return 0
        elif len(nums) == 1: total = nums[0]
        elif len(nums) == 2: total = max(nums)
        elif len(nums) == 3: total = max(nums[0] + nums[2], nums[1])
        return total
            

sol = Solution()
print(sol.rob([2,1,1,2]))
print(sol.rob([2,7,9,3,1,5,0,4,8]))