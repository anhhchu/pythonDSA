class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # divide intervals by half
        # base: len(intervals) == 2
        # compare 2 intervals:
            # if intervals[i-1][1] within intervals[i] 
            # => intervals = [[intervals[0][0]:intervals[1][1]]
            # else: return intervals
            
        # merge last interval of 1st half to first interval of 2nd half
        
        if len(intervals) <= 1:
            return intervals
        elif len(intervals) == 2:
            # check if 2nd val of first interval falls within 2nd interval
            if intervals[1][0] <= intervals[0][1] <= intervals[1][1]:
                # check 1st val of 1st interval also falls outside of 2nd interval
                if intervals[0][0] < intervals[1][0]:
                    intervals = [[intervals[0][0],intervals[1][1]]]
                # check 1st val of 1st interval falls within 2nd interval
                elif intervals[1][0] <= intervals[0][0] <= intervals[1][1]:
                    intervals = [intervals[1]]
            # check if 2nd val of first interval > 2nd val 2nd interval
            elif intervals[0][1] > intervals[1][1]:
                intervals = [[intervals[0][0], intervals[0][1]]]
            
            # cannot merge as no overlap
            return intervals
        
        mid = len(intervals)
        intervals = self.merge(intervals[:mid]) + self.merge(intervals[mid:])
        return intervals
        
    