# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # SOLUTION #1: DFS pre-order traversal. 
    # TC: O(N) + SC: O(N)
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     max_h = 0
    #     def dfs(node: Optional[TreeNode], h: int) -> None:
    #         if not node:
    #             return None
    #         nonlocal max_h
    #         max_h = max(max_h, h)
    #         dfs(node.left, h+1)
    #         dfs(node.right, h+1)
    #     dfs(root, 1)
    #     return max_h

    # SOLUTION #2: DFS post-order traversal
    # TC: O(N) + SC: O(N)
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs(node.right)
            return max(l, r) + 1
        return dfs(root)
