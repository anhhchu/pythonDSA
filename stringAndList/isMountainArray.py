class Solution:
    def validMountainArray(self, A):
        '''
        first loop to peak, 2nd loop to end of array => O(n) time, O(1) space
        '''
        if len(A) < 3:
            return False
        i = 1
        #peak = 0
        while i < len(A):
            if A[i-1] == A[i]:
                return False
            elif A[i-1] < A[i]:
                peak = i
                i += 1
            elif A[i-1] > A[i]:
                peak = i-1
                break
        
        if peak == 0 or peak >= len(A) - 1:
            return False
        
        while peak+1 < len(A):
            if A[peak] <= A[peak+1]:
                return False
            else:
                peak += 1
        
        return True

    def Test(self, A, expected):
        output = self.validMountainArray(A)
        if output == expected:
            return 'Pass'
        return 'Fail'


sol = Solution()

A = [2,1]
print(sol.Test(A, False))

A = [3,5,5]
print(sol.Test(A, False))

A = [0,3,2,1]
print(sol.Test(A, True))

A = [0,2,3,4,5,2,1,0]
print(sol.Test(A,True))

A = [0,2,3,3,5,2,1,0]
print(sol.Test(A,False))

A = [0,1,2,3,4,5,6,7,8,9]
print(sol.Test(A,False))

A = [5,4,3,2,1]
print(sol.Test(A,False))
            