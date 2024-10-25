class Solution:
    # SOLUTION: Binary Search
    # TC: O(log N) -- binary search.
    # SC: O(1) -- pointers only.
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(f"l: {l}, r: {r}, mid: {mid}, nums[mid]: {nums[mid]}")
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]: # l-mid sorted.
                if target >= nums[l] and target < nums[mid]: # target is somewhere between l-mid
                    r = mid - 1
                else: # target is not between l-mid
                    l = mid + 1
            else: # mid - r sorted
                if target > nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
        


