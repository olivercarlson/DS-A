class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # SOLUTION #1: Manual Addition
        # SC: O(N+M); TC: O(N+M)
        remainder = 0
        ptr_a = len(a) - 1
        ptr_b = len(b) - 1
        ans = deque()
        while ptr_a >= 0 or ptr_b >= 0 or remainder > 0:
            cur_a = a[ptr_a] if ptr_a >= 0 else "0"
            cur_b = b[ptr_b] if ptr_b >= 0 else "0"
            new_value = int(cur_a) + int(cur_b) + remainder
            remainder = 0
            while new_value > 1:
                new_value -= 2
                remainder += 1
            ans.appendleft(str(new_value))
            ptr_a -= 1
            ptr_b -= 1
        return "".join(ans)
