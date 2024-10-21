from functools import cache
class Solution:
    # SOLUTION #1: Top Down DP
    # TC: O(N * M) where M = amount and N = # of denominations
    # SC: O(S) for the call stack, where S is the input amount.
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        @cache
        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return -1
            min_val = math.inf
            for c in coins:
                res = dfs(rem - c)
                if res != -1:
                    min_val = min(min_val, res + 1)
            if min_val != math.inf:
                return min_val
            else:
                return -1
        return dfs(amount)
        