class Solution:

    # SOLUTION #1: set
    # TC: O(N), SC: O(N)
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set(nums)
        return len(s) != len(nums)
    
        