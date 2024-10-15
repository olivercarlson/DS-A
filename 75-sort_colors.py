class Solution:
    # SOLUTION #1:
    # TC: O(N) -- two pass, two processing of N where N = len(nums)
    # SC: O(1) -- store count of each item where count is 1 of 0,1,2
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hm = { 0: 0, 1: 0, 2: 0}

        for n in nums:
            hm[n] += 1
        for i in range(len(nums)):
            if hm[0] > 0:
                nums[i] = 0
                hm[0] -= 1
            elif hm[1] > 0:
                nums[i] = 1
                hm[1] -= 1
            else:
                nums[i] = 2
                hm[2] -= 1
        


            
