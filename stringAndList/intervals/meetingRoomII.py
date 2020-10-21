'''
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''

class Solution:
    def meetingRoomII(self, meetings):
        if meetings == [] or meetings == [[]]:
            return 0
        elif len(meetings) == 1: 
            return 1
        meetings.sort(key = lambda x: (x[0],x[1]))
        rooms = [meetings[0][1]] # keep the end time of meetings
        i = 1
        while i < len(meetings):
            start, end = meetings[i][0], meetings[i][1]
            if start < min(rooms): # need more rooms
                rooms.append(end)
            elif start >= min(rooms): # no overlap, use same room, update meeting end time
                rooms.remove(min(rooms))
                rooms.append(end)
            i += 1
        return len(rooms)

sol = Solution()
tests = [[[2,15],[36,45],[9,29],[16,23],[4,9]],[[7,10],[2,4]],[[6,16],[9,16],[1,9],[3,15]],[[0, 30],[5, 10],[15, 20]],[[7,10]], []]
for test in tests:
    print(sol.meetingRoomII(test))