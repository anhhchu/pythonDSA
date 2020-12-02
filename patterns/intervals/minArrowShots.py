"""
Minimum Number of Arrows to Burst Balloons
There are some spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter, and hence the x-coordinates of start and end of the diameter suffice. The start is always smaller than the end.


Given an array points where points[i] = [xstart, xend], return the minimum number of arrows that must be shot to burst all balloons.

Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Example 4:

Input: points = [[1,2]]
Output: 1
Example 5:

Input: points = [[2,3],[2,3]]
Output: 1
 

Constraints:

0 <= points.length <= 104
points.length == 2
-231 <= xstart < xend <= 231 - 1

"""

# sort and find overlapping range of intervals, return len of overlapping range
    # ex1: [[10,12],[2,8],[1,6],[7,13]]
        # [1,6], [2,8], [7,13], [10,12], n = 4
        # [2,6], [10,12], n = 2 return 2
    # ex2: [[1,2],[2,3],[3,4],[4,5]], n = 4
        #[2],[4] => return 2
    # ex3: [[1,2],[2,3],[2,4],[4,5]]
        # [2,2],[2,4] => [2,2] => return 1
    # ex4: [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
        # [6,7],[9,12]

class Solution:
    def findMinArrowShots(self,points):
        if len(points) <= 1:
            return len(points)
        points.sort(key = lambda x: x[1])
        
        # if end of the previous intervals not contained in subsequent intervals, increase count 
        # [[6, 7], [3, 9], [6, 9], [1, 10], [4, 11], [8, 12], [9, 12]]

        prev_end = points[0][1] # 7
        count = 1 # count = 7
        for point in points: # [4,11], count = 3
            start = point[0] # 4
            #end = point[1]
            # 10 vs. 4
            if prev_end < start:
                count+=1 # count = 3
                prev_end = point[1] # 11
        return count 


    def findMinArrowShotsMergeIntervals(self, points):
        if len(points) <= 1:
            return len(points)
        points.sort() # NlogN
        #[1,6], [2,8], [7,13], [10,12]
        prev_start = points[0][0] # 1
        prev_end = points[0][1] # 6
        i = 1
        while i < len(points): # i = 2
            # prev_start = 7, prev_end = 13
            start = points[i][0] # 10
            end = points[i][1] # 12
              
            if prev_end < start: 
                i += 1 # go to next interval and update prev_start, prev_end
                prev_start = start
                prev_end = end
                    #13        #10    
            elif prev_end >= start: #merge intersect [start, min(prev_end, end)]
                points[i-1] = [start, min(prev_end,end)] # [10,12]
                # don't increment i but remove point at index i and update prev_start 
                points.pop(i)
                prev_start = start # 10
                prev_end = min(prev_end, end) # 12
           
            # points =  [2,6], [10,12]
        
        return len(points)

            


sol = Solution()
#points = [[1, 10], [3, 9], [4, 11], [6, 7], [6, 9], [8, 12], [9, 12]]
points = [[10,12],[2,8],[1,6],[7,13]]
print(sol.findMinArrowShots(points) )  