'''
Given an array of integers, find out 
whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] 
is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        This is an O(n^2) solution => improve to O(nlogk) or O(n) solution
        """
        self.nums, self.k, self.t = nums, k, t
        i = 0
        #j = i+k
        while i < len(nums):
            
            m = i + 1
            j = i + k 
            #print(i, m, j)

            while m <= j and m < len(nums): 
                #print(abs(nums[i] - nums[m]))
                if abs(nums[i] - nums[m]) <= t:
                    return True
                m += 1
            i += 1

        return False

    def test(self, nums, k, t, expected):
        output = self.containsNearbyAlmostDuplicate(nums, k, t)
        print(output)
        if output == expected:
            return "Pass"
        return "Fail"



sol = Solution()
nums = [1,2,3,1]
k, t = 3, 0
print(nums, sol.test(nums, k, t, True))

nums = [1,0,1,1]
k, t = 1, 2
print(nums, sol.test(nums, k, t, True))

nums = [1,5,9,1,5,9]
k, t = 2, 3
print(nums, sol.test(nums, k, t, False))

nums = [2,2]
k, t = 3, 0
print(nums, sol.test(nums, k, t, True))


######
print('SOLUTION 2 - USE HASH TABLE')

class Solution2(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool

        Improve to O(nlogk) OR O(k) solution, O(n) space
        design a hashtable and hold the upper bound and lower bound information of the element in nums compared to t as key, 
        index of the element in nums as value dict = {(val-t, val+t), index}

        iterate over elements in nums: 
        * if element within the bound 
            * if index of element - dict[key] < k -> True
            * else update {(lower, upper bound), index} of the new element in dict
        * else: go to next element 

        if no element left to check in nums -> False
        """
        import collections
        seen = collections.OrderedDict()

        for i, val in enumerate(nums):
            upperbound = max(val-t, val+t)
            lowerbound = min(val-t, val+t)
            #print(seen)
            for lb, ub in seen: 
                if i - seen[(lb, ub)] > k or i - seen[(lb, ub)] == 0:
                    seen.pop((lb, ub))
                elif lb <= val <= ub:
                    if 0 < (i - seen[(lb,ub)]) <= k: 
                        return True
                    else: 
                        seen.pop((lb, ub))
                        break
                        #seen[(lowerbound, upperbound)] = i
            seen[(lowerbound, upperbound)] = i
        #print(seen)
        return False

    def test(self, nums, k, t, expected):
        output = self.containsNearbyAlmostDuplicate(nums, k, t)
        print(output)
        if output == expected:
            return "Pass"
        return "Fail"


sol = Solution2()
nums = [1,2,3,1]
k, t = 3, 0
print(sol.containsNearbyAlmostDuplicate(nums, k, t))
print(nums, sol.test(nums, k, t, True))

nums = [1,0,1,1]
k, t = 1, 2
print(nums, sol.test(nums, k, t, True))

nums = [1,5,9,1,5,9]
k, t = 2, 3
print(sol.containsNearbyAlmostDuplicate(nums, k, t))
print(nums, sol.test(nums, k, t, False))

nums = [2,2]
k, t = 3, 0
print(nums, sol.test(nums, k, t, True))

nums = [3,6,0,4]
k, t = 2, 2
print(nums, sol.test(nums, k, t, True))
