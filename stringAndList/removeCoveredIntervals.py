class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        can go up to O(N^2), O(1) space
        """
        
        if len(intervals) == 1:
            return len(intervals)
            
        # sort intervals
        intervals.sort(key = lambda x: (x[0], x[1])) #O(n)
   
        i = len(intervals) - 2
        j = len(intervals) - 1
        while i >= 0:
            for j in range(len(intervals)-1, i,-1) :
                if intervals[j][0] == intervals[i][0]:
                    if intervals[j][1] >= intervals[i][1]:
                        intervals.pop(i)
                        break
            
                elif intervals[i][0] < intervals[j][0] <= intervals[i][1]:
                    if intervals[j][1] <= intervals[i][1]: 
                        intervals.pop(j)
            i -= 1
            
        return len(intervals) 

    def removeCoveredIntervalsOpt(self, intervals):
        """
        O(nLogn) time, O(n) space
        """
        if len(intervals) == 1:
            return len(intervals)

        intervals.sort(key=lambda x: (x[0],-x[1])) # sort ascending first then descending for 2nd element
        
        count = 0
        prev_end = 0

        for _, end in intervals:
            if end > prev_end:
                count += 1
                prev_end = end

        return count


sol = Solution()
print(sol.removeCoveredIntervals([[3,10],[4,10],[5,11]]))
print(sol.removeCoveredIntervalsOpt([[3,10],[4,10],[5,11]]))

