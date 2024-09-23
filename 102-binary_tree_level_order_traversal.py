# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # SOLUTION #1: BFS
        # TC: O(N), SC: O(N)
        ans = []

        q = deque([root])
        level = []
        cur = []
        while q:
            node = q.popleft()
            if not node: 
                break
            cur.append(node.val)
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)
            if not q:
                ans.append(cur)
                cur = []
                q = deque(level)
                level = []
        return ans