class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        if len(intervals) < 2:
            return True

        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                return False

        return True
