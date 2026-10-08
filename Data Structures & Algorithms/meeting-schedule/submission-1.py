"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        s = set()
        for time in intervals:
            i = time.start
            while i < time.end:
                if i in s:
                    return False
                s.add(i)
                i = i+1
        return True