class Solution:
    # Solution #1: Stack
    # TC: O(N) - must iterate through all chars
    # SC: O(N) - stack to store all numbers at once which is ~= N / 2
    def evalRPN(self, tokens: List[str]) -> int:
        ops = { 
            '+': lambda a,b: b+a, 
            '-': lambda a,b: b-a,
            '/': lambda a,b: int(b/a),
            '*': lambda a,b: b*a
            }

        s = []
        for t in tokens:
            if len(t) > 1 and t[0] in ops:
                s.append(int(t))
            elif t[0] in ops:
                v1 = s.pop()
                v2 = s.pop()
                val = ops[t](v1,v2)
                s.append(val)
            else:
                s.append(int(t))
        return s[0]
    