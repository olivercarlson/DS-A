# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    # SOLUTION #1:
    # DFS pre-order, does NOT take advantage of the fact that it is a BST / input is sorted.
    # TC: O(N) best/worst case, SC: O(N + K) - call stack for entire tree + 
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     h = []
    #     def dfs(node) -> None:
    #         nonlocal h
    #         nonlocal k
    #         if not node:
    #             return None
    #         if len(h) < k:
    #             heapq.heappush(h, -node.val)
    #         else:
    #             heapq.heappushpop(h, -node.val)
    #         dfs(node.left)
    #         dfs(node.right)
    #         return
    #     dfs(root)
    #     return -h[0]
    
    # SOLUTION #2:
    # DFS in-order, does take advantage of the fact that input is sorted / BST.
    # TC: O(N) worst case (where k == size largest element in tree), best case O(log N)  SC: O(H) for the call stack -- worst case SC: O(N) (skewed tree), O(log N) average/best case.
        def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
            ans = None
            self.k = k
            # travel all the way down the left of the bst.
            # in order traversal
            def dfs(node: Optional[TreeNode]) -> None:
                nonlocal ans
                if ans is not None or not node:
                    return
                
                dfs(node.left)
                self.k -= 1
                if self.k == 0:
                     ans = node.val
                     return None
                dfs(node.right)

            dfs(root)
            return ans
