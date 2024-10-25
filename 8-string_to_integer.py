class Solution:
    # SOLUTION #1: an absolute abomination
    # TC: O(N) -- process all characters in char individually.
    # SC: O(N) -- worst case storing string of size N in temp variable (res).
    def myAtoi(self, s: str) -> int:
        sign = None
        res = ""
        for ch in s:
            if len(res) == 0:
                if ch == " " and sign is None:
                    continue
                elif (ch == "+" or ch == "-") and sign is None:
                    sign = ch‹
                elif ch.isnumeric():
                    res += ch
                else:
                    break
            elif len(res) > 0:
                if ch.isnumeric():
                    res += ch
                else:
                    break
        if len(res) == 0:
            return 0
        ans = int(res)
        if sign == "-":
            ans = -ans
        if ans > 2 ** 31 - 1:
            return 2 ** 31 - 1
        if ans < -2 ** 31:
            return -2 ** 31

        return ans
    