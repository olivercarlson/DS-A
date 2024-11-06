class Solution:
    # SOLUTION: Sliding window.
    # TC: O(N) -- single pass
    # SC: O(1) -- only pointers
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return max_area

