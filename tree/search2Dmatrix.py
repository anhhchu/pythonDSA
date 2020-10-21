class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False 
        
        m, n = len(matrix), len(matrix[0])
        # search a flatten matrix: row = idx//n, col = idx%n
        # do binary search on virtual flatten matrix
        start = 0
        end = m*n-1
        while start <= end:
            mid = (start+end)//2
            row, col = mid//n, mid%n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid-1
            elif matrix[row][col] < target:
                start = mid+1
        return False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))