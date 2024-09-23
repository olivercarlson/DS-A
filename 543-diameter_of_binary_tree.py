# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # SOLUTION #1: Post Order Traversal
        # TC: O(N) -- all nodes visited at most one time, SC: O(N) -- call stack in case of unbalanced tree.
        diameter = 0
        def dfs(node: Optional[TreeNode], height: int) -> int:
            nonlocal diameter

            if not node: 
                return height

            height_l = dfs(node.left, 0)
            height_r = dfs(node.right, 0)

            diameter = max(diameter, height_l + height_r)
            
            return max(height_l, height_r) + 1
    
        dfs(root, 0)
        return diameter