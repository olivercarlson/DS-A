# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # SOLUTION #1: Fancy DFS recursion
    # TC: O(N) -- process all nodes at least once
    # SC: O(N) -- call stack for recursion
    def validate(self, node, low=-math.inf, hi=math.inf) -> bool:
        if not node:
            return True
        if node.val <= low or node.val >= hi:
            return False
        return self.validate(node.left, low, node.val) and self.validate(node.right, node.val, hi)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root)
    
    # SOLUTION #2: DFS inorder traversal by being sneaky.
    # TC: O(N) -- must iterate through all nodes at least once.
    # SC: O(N) -- call stack.
    def dfs(self, node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        if not self.dfs(node.left):
            return False
        if node.val <= self.prev:
            return False
        self.prev = node.val
    return self.dfs(node.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = -math.inf
        return self.dfs(root)