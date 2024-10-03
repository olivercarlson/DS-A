class Solution:
    # SOLUTION #1: Using division, a now disallowed tactic by problem statement.
    # TC: O(N): Tow passes through the dataset.
    # SC: O(N) if the size of the return array counts. Else it's O(1) since only the answer and two ints are used.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # multiply all nums together, store product value:
            # if numzeros >= 2: all values 0.
            # if numzeros == 0: proceed regularly
            # if numzeros == 1: all values are zero except the zero location
        prod = 1
        zero_count = 0
        ans = [0]  * len(nums)
        for n in nums:
            # n != 0
            if n != 0:
                prod *= n
                continue
            # n == 0
            zero_count += 1
            if zero_count == 1:
                continue
            else:
                return ans
            prod *= n
        for i,n in enumerate(nums):
            if zero_count == 0:
                ans[i] = prod // n
            elif n == 0:
                ans[i] = prod
        return ans
    # SOLUTION #2: Following the rules, two pass, one forwards, one backwards
    # TC: O(N) two passes through the data with some pointers O(2*N) ~= O(N)
    # SC: O(N) or O(1) depending on whether or not answer counts. Given that problem states to create new array, should commonly be described as O(1)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod = 1
        ans = [1] * len(nums)
        for i,n in enumerate(nums):
            ans[i] *= prefix_prod
            prefix_prod *= n
        postfix_prod = 1
        for i in range(len(nums) - 1, -1,-1):
            ans[i] *= postfix_prod
            postfix_prod *= nums[i]
        return ans