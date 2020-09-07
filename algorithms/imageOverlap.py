'''
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)

We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes: 

1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
'''
import collections
class Solution:
     def largestOverlap(self, A, B):
          '''
          type A: List[List[int]] 
          type B: List[List[int]]
          rtype: int, largest possible overlap
          '''

          A = [(i,j) for i, row in enumerate(A) for j, item in enumerate(row) if item]
          B = [(i,j) for i, row in enumerate(B) for j, item in enumerate(row) if item]
          count = collections.Counter((ax-bx, ay-by) for ax, ay in A for bx, by in B)

          print(A)
          print(B)
          print(count)

          return max(count.values() or [0])
          


sol = Solution()

A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,1,1],[0,0,1]]
print(sol.largestOverlap(A,B))

A = [[1,1,0],[0,1,0],[0,1,0]]
B = [[0,0,0],[0,0,0],[0,0,0]]
print(sol.largestOverlap(A,B))


