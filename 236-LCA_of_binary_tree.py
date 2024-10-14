# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # SOLUTION #1: DFS
    # TC: O(N) - at worst process every node in tree once.
    # SC: O(N) - # of functional calls in stack == number of nodes in tree.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = 0
        def dfs(node: Optional['TreeNode']):
            nonlocal ans
            if not node:
                return False
            # root is p or q: root is ans
            # either node is p or q and node.left contains p || q and node.right contains p || q
            mid = node == p or node == q
            left = dfs(node.left)
            right = dfs(node.right)
            if left + right + mid > 1:
                ans = node
            return mid or left or right
        dfs(root)
        return ans