class Solution:
    # SOLUTION #1: DFS
    # TC: O(N) -- visit each node once
    # SC: O(H) -- where H is the height of the binary tree. in case of skewed tree, H == N.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def dfs(node, h):
            if not node:
                return ans
            if len(ans) <= h:
                ans.append(node.val)
            dfs(node.right, h + 1)
            dfs(node.left, h + 1)
            return ans
        return dfs(root, 0)
class Solution:
    # SOLUTION #2: BFS
    # TC: O(N) -- process each node at most once.
    # SC: O(D) -- where D is the size of the deque -- which is the tree's diameter, at the largest level. in balanced tree, this is ~N/2 ~= N.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        d = deque([[root, 0]])
        while d:
            node, h = d.popleft()
            if len(ans) <= h:
                ans.append(node.val)
            if node.right:
                d.append([node.right, 1+h])
            if node.left:
                d.append([node.left, 1+h])            
        return ans
