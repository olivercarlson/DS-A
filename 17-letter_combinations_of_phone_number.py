class Solution:
    # SOLUTION: backtracking.    
    # TC: O(4 ** N * N) where N = len(digits). worst case digits are only 7s/9s -- for each digit, 4 calculations per additional digit * total number of digits processed.
    # SC: O(N) -- where N is length of digits (maximum depth of call stack). Ignoring size of the output array.
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        #digits = 2-9 inclusive
        d_to_l = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        ans = []
        def bt(s: str, pos: int) -> List[str]:
            nonlocal digits
            nonlocal ans
            if len(s) == len(digits):
                ans.append(s)
                return

            current_letters = d_to_l[digits[pos]]
            for ch in current_letters:
                if pos < len(digits):
                    bt("" + s + ch, 1 + pos)
        bt("", 0)
        return ans