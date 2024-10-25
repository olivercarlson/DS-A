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
    # SOLUTION #2: cleaned up code based off of soln. sign usage and checking MUCH improved.
    # TC: O(N) -- process all chars in s
    # SC: O(1) -- never using intermediate str allows up to keep space usage minimal.
    def myAtoi(self, s: str) -> int:
        MAX_INT = pow(2,31) - 1
        MIN_INT = -pow(2,31)


        sign = 1
        res = 0
        idx = 0

        # handle leading whitespace
        while idx < len(s) and s[idx] == " ":
          idx += 1

        # handle sign
        if idx < len(s) and s[idx] == "+":
            sign = 1
            idx += 1
        elif idx < len(s) and s[idx] == "-":
            sign = -1
            idx += 1

        # handle digits
        while idx < len(s) and s[idx].isdigit():
            digit = int(s[idx])
            if res > MAX_INT // 10 or (res  == MAX_INT // 10 and digit > MAX_INT % 10):
                return MAX_INT if sign == 1 else MIN_INT
            res = 10 * res + digit
            idx += 1

        return sign * res