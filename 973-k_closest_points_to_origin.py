class Solution:
    # SOLUTION #1: (Max) Heap
    # TC: O(N log k) -- O(N) for iteration over points. N log k for adding items to heap
    # SC: O(k) -- only store K elements in heap.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for x,y in points:
            d = x**2 + y**2
            if len(h) < k:
                heapq.heappush(h, [-d,x,y])
            else:
                heapq.heappushpop(h, [-d,x,y])
        ans = []
        while h:
            d, x,y = heapq.heappop(h)
            ans.append([x,y])
        return ans
    # SOLUTION #2: Quick Select
    # TC: O(N) -- average case. Worst Case O(N^2) - sorted or nearly sorted points.
    # SC: O(log N) -- average case due to number of recursive calls whiddling down size of N. O(N) -- worst case due to call stack from N calls in sorted or nearly sorted list of points.
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def pivot(arr, pivot_index, end_index):
            swap_index = pivot_index

            for i in range(pivot_index + 1, end_index+1):
                x,y = arr[i]
                d = x ** 2 + y ** 2
                px, py = arr[pivot_index]
                pd = px ** 2 + py ** 2
                if d <= pd:
                    swap_index += 1
                    arr[i], arr[swap_index] = arr[swap_index], arr[i]
            arr[swap_index], arr[pivot_index] = arr[pivot_index], arr[swap_index]
            return swap_index

        def qs(arr, l,r):
            nonlocal k
            if l < r:
                pivot_index = pivot(arr,l,r)
                if k == pivot_index:
                    return
                elif k > pivot_index:
                    qs(arr, pivot_index + 1,r)
                else:
                    qs(arr, l, pivot_index - 1)
            return
        
        qs(points,0,len(points) - 1)
        return points[:k]
    # SOLUTION #3: Quick Select from LC Editorial
    # TC: O(N) avg, O(N**2) worst
    # SC: O(1)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
            return self.quick_select(points, k)
    def quick_select(self, points: List[List[int]], k: int) -> List[List[int]]:
        left, right = 0, len(points) - 1
        pivot_index = len(points)
        while pivot_index != k:
            pivot_index = self.partition(points, left, right)
            if pivot_index < k:
                left = pivot_index
            else:
                right = pivot_index - 1
        return points[:k]
    def partition(self, points: List[List[int]], l: int, r: int) -> int:
        pivot = points[l + (r - l) // 2]
        pivot_dist = self.squared_distance(pivot)
        while l < r:
            if self.squared_distance(points[l]) >= pivot_dist:
                points[l], points[r] = points[r], points[l]
                r -= 1
            else:
                l += 1
        if self.squared_distance(points[l]) < pivot_dist:
            l += 1
        return l
    def squared_distance(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2