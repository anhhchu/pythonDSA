'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''

class Solution:
    def checkIfExist(self, arr):
        '''
        O(N) time, O(N) space
        '''
        arrDouble = []
        for num in arr: 
            if num >= 0:
                arrDouble.append(num*2)
            else:
                if abs(num)*2 not in arrDouble or num*2 not in arrDouble:
                    arrDouble.append(abs(num)*2)
                    arrDouble.append(num*2)
        print(arrDouble)
        for num in arrDouble:
            if num in arr:
                return True
        return False
        

def test(arr, expected):
    sol = Solution()
    output = sol.checkIfExist(arr)
    if output == expected:
        return 'Pass'
    return 'Fail'


arr = [10,2,5,3,5,10,0]
print(test(arr, True))
arr = [-2,0,10,-19,4,6,-8]
print(test(arr, True))
arr = [3,1,7,11]
print(test(arr, False))
arr = [-10,12,-20,-8,15]
print(test(arr, True))
arr = [18,-6,-9,17]
print(test(arr, True))
