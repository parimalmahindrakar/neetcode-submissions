class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])   
        keep = 0
        prev_end = float("-inf")

        for interval in intervals:
            if prev_end <= interval[0]:
                keep += 1
                prev_end = interval[1]
            
        return len(intervals) - keep

        