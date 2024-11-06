from functools import cache

class Solution:
    # SOLUTION:
    # TC: O(N ** 2) -- worst case where N == input string of all the same char, process all input N * N.
    # SC: O(1)  -- only pointers.
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        ans = (0,0)

        @cache
        def expand(l,r):
            nonlocal ans
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    if r - l > ans[1] - ans[0]:
                        ans = (l,r)
                    l -= 1
                    r += 1
                else:
                    return
        
        for i in range(len(s)):
            if i >= len(s) - 1:
                break
            if s[i] == s[i+1]:
                expand(i, i+1)
            if i >= 1 and s[i-1] == s[i+1]:
                expand(i-1, i+1)

        return s[ans[0]:ans[1]+1]

