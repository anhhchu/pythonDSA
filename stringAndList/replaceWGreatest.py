'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
'''

class Solution:
    def replaceElements(self, arr):
        if len(arr) < 1:
            return arr
        if len(arr) == 1:
            return [-1]
        if len(arr) == 2:
            arr[0] = arr[-1]
            arr[-1] = -1
            return arr

        carry = arr[-1]
        for i in range(len(arr)-3, -1, -1): 
            #print(i, carry)
            temp = arr[i]
            #print(temp)
            arr[i] = max(carry, arr[i+1], arr[i+2]) 
            carry = temp
            
        
        arr[-2] = arr[-1]
        arr[-1] = -1

        return arr

sol = Solution()
print(sol.replaceElements([17,18,5,4,6,1]))
print(sol.replaceElements([17,18]))
print(sol.replaceElements([-2,-3,0]))
print(sol.replaceElements([]))

