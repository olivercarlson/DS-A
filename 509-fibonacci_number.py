class Solution:
    # SOLUTION #1: top down
    # TC: O(2N - 1) ~= O(N)
    # SC: O(2N - 1) ~= O(N)
    def __init__(self):
        self.memo = {0:0, 1:1}

    def getFib(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.getFib(n-1) + self.getFib(n-2)
        return self.memo[n]

    def fib(self, n: int) -> int:
        return self.getFib(n)
    # SOLUTION #2: bottom up
    # TC: O(N)
    # SC: O(N)
    def fib(self, n: int) -> int:
        dp = [0,1]
        for x in range(2,n+1):
            dp.append(dp[x-1] + dp[x-2])
        return dp[n]