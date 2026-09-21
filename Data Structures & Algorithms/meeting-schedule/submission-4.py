"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals: return True
        # if we sort by start times, there is an overlap
        # between two intervals if end_1 > start_2
        # this holds true for any latter intervals as well

        sorted_ints = sorted(intervals, key = lambda x: x.start)
        prev_end = sorted_ints[0].end
        for interval in sorted_ints[1:]:
            if interval.start < prev_end:
                return False
            prev_end = interval.end


        return True
