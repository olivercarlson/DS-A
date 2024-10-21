class TimeMap:
    # SOLUTION #1: array + binary search. always nice getting the optimal solution on the first try.
    # TC: O(log N) -- binary search for get. O(1) for set.
    # SC: O(N) or O(1) depending on how we count the actual storage. Given that we are using a tuple.
    def __init__(self):
        # dict key : heapq with timestamps -> value    
        # dict of tuples, binary search to get?
        self.d = {}
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = []
        self.d[key].append((timestamp, value))
        return None
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        k = self.d[key]
        l = 0
        r = len(k) - 1

        while l < r:
            mid = (r + l) // 2
            if k[mid][0] == timestamp:
                return k[mid][1]
            elif k[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if k[l][0] <= timestamp:
            return k[l][1]
        if l - 1 >= 0 and k[l-1][0] < timestamp:
            return k[l-1][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)