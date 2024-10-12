from copy import deepcopy

class Combo:
    def __init__(self, c):
        self.combo = Counter()
        self.csum = c
        self.combo[c] = 1

class Solution:
    # SOLUTION #1: BFS using custom combo object. a mess.
    # TC: O(N ** T/M+1) -- worst case is to process all nodes to maximum depth of tree which is target / minimum node value.
    # SC: O(T/M) -- worst case would be deque of size T/M?
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = {}
        d = deque()    
        for c in candidates:
            if c == target:
                d.append(Combo(c))
            if c < target and c > 0:
                new_combo = Combo(c)
                new_combo.csum = c
                d.append(new_combo)
        while d:
            combo = d.popleft()
            if combo.csum == target:
                ele = sorted(combo.combo.elements())
                new_ans = []
                for n in ele:
                    new_ans.append(n)
                ans[f"{new_ans}"] = new_ans
            elif combo.csum < target:
                for c in candidates:
                    if combo.csum + c <= target:
                        new_copy = deepcopy(combo)
                        new_copy.csum += c
                        if c not in new_copy.combo:
                            new_copy.combo[c] = 0
                        new_copy.combo[c] += 1
                        d.append(new_copy)
        return [n for n in ans.values()]
        # SOLUTION #2: DFS / Backtracking:
        # TC: O(N ** T / M + 1) -- where N = # candidates, T = target value, M is minimum candidate value. 
            # Maximal depth of the tree would be T / M -- adding smallest possible element to combination to reach (or stop execution by exceeding target)
                # maximal number of nodes in N-ary tree of T/M height = N ** T/M+1
        # SC: O(T/M) for call stack (also current path).
        def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            def dfs(i, path, csum):
                if csum == target:
                    ans.append(path)
                    return
                if csum > target or i >= len(candidates):
                    return
                dfs(i, [candidates[i]] + path, candidates[i] + csum)
                dfs(i+1, path, csum)

            ans = []
            dfs(0, [], 0)
            return ans  