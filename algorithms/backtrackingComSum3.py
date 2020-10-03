'''
# Backtracking Algorithms
Backtracking is an algorithmic-technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time (by time, here, is referred to the time elapsed till reaching any level of the search tree).

# Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

Complexity Analysis

Let K be the number of digits in a combination.

Time Complexity: O(9!*K/(9-K)!)

In a worst scenario, we have to explore all potential combinations to the very end, i.e. the sum n is a large number (n > 9 ). At the first step, we have 99 choices, while at the second step, we have 88 choices, so on and so forth.

The number of exploration we need to make in the worst case would be P(9, K) = 9!/(9-K)!
 , assuming that K <= 9*K <=9. By the way, K cannot be greater than 9, otherwise we cannot have a combination whose digits are all unique.

Each exploration takes a constant time to process, except the last step where it takes O(9!*K/(9-K)!) time to make a copy of combination.

To sum up, the overall time complexity of the algorithm would be 


Space Complexity: O(K)

During the backtracking, we used a list to keep the current combination, which holds up to KK elements, i.e. O(K).

Since we employed recursion in the backtracking, we would need some additional space for the function call stack, which could pile up to K consecutive invocations, i.e. O(K).

Hence, to sum up, the overall space complexity would be O(K).

Note that, we did not take into account the space for the final results in the space complexity.
'''
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(remaining, comb, startIdx):
            # condition where the combination is found
            if remaining == 0 and len(comb) == k: 
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                result.append(list(comb))
                #print('intermediate result', result)
                return
            
            # condition where we exit the current branch
            elif remaining < 0 or len(comb) == k: 
                return 
        
            for i in range(startIdx, 10):
                #print('i',i) 
                comb.append(i) # we want to append the next value
                #print('comb', comb)
                backtrack(remaining-i, comb, i+1)
                # remember to remove the last element for the next backtracking branch
                comb.pop()
                #print('next comb', comb)

        backtrack(n,[],1) # calling backtrack for the first time


        return result

    def combinationSum3Opt(self, k, n):

        from itertools import combinations

        candidates = combinations(range(1,10), k) # create a permutation of candidate pool of length k
        result = []
        for option in candidates:
            if sum(option) == n:
                result.append(option)
            
        return result



sol = Solution()
'''
print(sol.combinationSum3(3,9)) #[[1,2,6],[1,3,5],[2,3,4]]
print(sol.combinationSum3(3,7)) # [[1,2,4]]
print(sol.combinationSum3(4,1)) # []
print(sol.combinationSum3(3,2)) # []
print(sol.combinationSum3(9,45)) # [[1,2,3,4,5,6,7,8,9]]
'''
print(sol.combinationSum3Opt(3,9)) #[[1,2,6],[1,3,5],[2,3,4]]
print(sol.combinationSum3Opt(3,7)) # [[1,2,4]]
print(sol.combinationSum3Opt(4,1)) # []
print(sol.combinationSum3Opt(3,2)) # []
print(sol.combinationSum3Opt(9,45)) # [[1,2,3,4,5,6,7,8,9]]

        
