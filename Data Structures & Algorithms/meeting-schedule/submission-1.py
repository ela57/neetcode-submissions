"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        hashs = set()
        for inter in (intervals):
            s = inter.start
            e = inter.end
            for hs, he in (hashs):
                if hs <= s < he or hs <= e < he:
                    return False
            hashs.add((s,e))
        return True