class Solution:
    # SOLUTION: Sliding Window / Two Pointer
    # TC: O(N) iteration through s
    # SC: O(1) since maximum size of seen is: alphabet (upper + lower) + spaces + symbols = 52 + space + symbols ~= 65?
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_ss = 0
        seen = {}
        for r in range(len(s)):
            if s[r] in seen:
                l = max(l,seen[s[r]] + 1)
            cur = s[l:r+1]
            max_ss = max(len(cur), max_ss)
            seen[s[r]] = r
        return max_ss