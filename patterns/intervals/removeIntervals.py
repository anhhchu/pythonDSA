'''
Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
Example 3:

Input: intervals = [[-5,-4],[-3,-2],[1,2],[3,5],[8,9]], toBeRemoved = [-1,4]
Output: [[-5,-4],[-3,-2],[4,5],[8,9]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
'''

class Solution:
    def removeInterval(self, intervals, toBeRemoved):
        # no overlap: [start, end]
        # toBeRemoved inside interval: [start, R1] [R2, end]
        # toBeRemoved is to the left of interval: [R2, end]
        # toBeRemoved is to the right of interval: [start, R1]
        # use extra space to store output, O(nlogn) time
        
        '''
        R1, R2 = toBeRemoved[0], toBeRemoved[1]
        i = 0
        while i < len(intervals):
            start, end = intervals[i][0], intervals[i][1]
            if end <= R1 or start >= R2:
                i += 1
            elif (start > R1 and end < R2) or (start == R1 and end == R2):
                intervals.pop(i)
            elif start < R1 and end > R2:
                intervals[i] = [start, R1]
                intervals.insert(i+1,[R2, end])
                i += 2
            elif R1 <= start <= R2 and end > R2:
                intervals[i] = [R2, end]
                i += 1
            elif start < R1 and R1 <= end <= R2:
                intervals[i] = [start, R1]
                i += 1
            else:
                i+=1
        intervals.sort() 
        return intervals
        '''
        r1, r2 = toBeRemoved[0], toBeRemoved[1]
        output = []
        for start, end in intervals:
            if start >= r2 or end <= r1: 
                output.append([start, end])
            elif r1 > start and r2 < end:
                output.append([start, r1])
                output.append([r2, end])
            elif r1 <= start and r2 < end:
                output.append([r2, end])
            elif r1 > start and r2 >= end:
                output.append([start, r1])
                
        output.sort()
        return output
        
                
        