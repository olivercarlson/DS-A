class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    
    # SOLUTION #1: Suboptimal Space
        # TC: O(N), SC: O(N)
        counter = Counter(nums)
        return max(counter.keys(), key=counter.get)

    # SOLUTION #2: Boyer-Moore
        # TC: O(N), SC: O(1)
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n
            count += 1 if candidate == n else -1
        return candidate