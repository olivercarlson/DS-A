class Solution:
    # Solution #1: TC: O(n log n) -- sorting operation. SC: O(n) -- sorting (Timsort) worst case. 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        merged = []
        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1][1] = max(merged[-1][1], intervals[i][1]) 
        return merged

    # Solution #2: TC worst case: O(n log n) -- Using a heap could potentially be significantly faster than any Timsort based solutions -- which are guaranteed to incur an O(n log n) cost.
    # With sorted or nearly sorted input intervals with large overlaps -- TC could be O(n) or O(n log k) where k is the size of the merged output.  
    # SC: worst case O(n) -- auxillary space from storing items in the heap. Potentially O(k) auxillary space where k is the size of the merged intervals - if k is very small, this is significant.
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = []
        for start,end in intervals:
            if h and ((h[0][0] >= start and h[0][0] <= end) or (h[0][1] >= start and h[0][1] <= end)):
                h[0][0] = min(h[0][0], start)
                h[0][1] = max(h[0][1], end)
            else:
                heapq.heappush(h, [start,end])
        ans = []
        while h:
            if not ans or ans[-1][1] < h[0][0]:
                ans.append(heapq.heappop(h))
            else:
                ans[-1][1] = max(ans[-1][1], heapq.heappop(h)[1])
        return ans
 
    # TODO: add solution #3 -- merge tree
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
