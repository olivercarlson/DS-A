class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # TC: O(N), SC: O(N) or O(1) depending on whether size of returned item is counted.
        if not intervals:
            return [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals
        if newInterval[0] > intervals[-1][1]:
            return intervals + [newInterval]
        left = []
        right = []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        return left + [newInterval] + right
