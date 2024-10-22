class Solution:
    # SOLUTION: backtracking
    # TC: apprxomiately O(N * N!) -- for each number N, there are N-1 combinations (~= N!). And with each of those we do O(N) lookup for n in curr
    # SC: O(N) -- recursion call stack -- where maximum depth of the call stack is == N (excluding size of answer array). 
    def permute(self, nums: List[int]) -> List[List[int]]:
        def bt(curr):
            if len(curr) == len(nums):
                ans.append([] + curr)
                return
            for n in nums:
                if n not in curr:
                    curr.append(n)
                    bt(curr)
                    curr.pop()

        ans = []
        bt([])
        return ans

