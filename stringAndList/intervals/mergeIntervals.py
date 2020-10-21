'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:

intervals[i][0] <= intervals[i][1]
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        O(NlogN) where N is the length of intervals 
        O(1) space, no additional space used
        """
        # start > prev_start, no overlapping
        # start == prev_start
            # end <= prev_end, merge with start and end of prev interval, pop interval 
            # end > prev_end, merge with prev_start of prev interval, end of current interval
        
        if len(intervals) <= 1:
            return intervals
        
        #intervals.sort(key = lambda x: (x[0],x[1]))
        intervals.sort() # O(NlogN)
        
        prev_start, prev_end = intervals[0][0], intervals[0][1]
    
        i = 1
        while i < len(intervals): # O(N)
      
            start = intervals[i][0]
            end = intervals[i][1]
      
            if start > prev_end:
                prev_start = start
                prev_end = end
                i += 1
                
            elif start == prev_start or start <= prev_end:
           
                if end <= prev_end: 
                    intervals.pop(i) # prev_start, prev_end stay the same
                    
                elif end > prev_end: 
                    intervals[i-1][1] = end # change value of prev_end
                    prev_end = end
                    intervals.pop(i)

        return intervals
    