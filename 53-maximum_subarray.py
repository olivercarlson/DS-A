class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #SOLUTION #1:
        # TC: O(N), SC: O(1)
        curSum = maxSum = nums[0] if len(nums) > 0 else 0

        for n in nums[1:]: # technically since this is a slice, this is actually a duplicate of nums, so this actually SC: O(N)
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)

        return maxSum
    
    # Slightly tweaked SOLUTION #1 to use no real extra space.
    # class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    #     curSum = maxSum = nums[0] if len(nums) > 0 else 0

    #     for n in range(1,len(nums)):
    #         if curSum < 0:
    #             curSum = 0
    #         curSum += nums[n]
    #         maxSum = max(maxSum, curSum)

    #     return maxSum
