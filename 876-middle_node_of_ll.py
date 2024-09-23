# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

# SOLUTION #1: extra space
        # TC: O(N), SC: O(N)
        # nodes = []
        # tmp = head
        # while tmp:
        #     nodes.append(tmp)
        #     tmp = tmp.next
        # return nodes[len(nodes) // 2]

        # SOLUTION #2: two pointer
        # TC: O(N), SC: O(N)
        slow = fast = head
        f_count = 0
        s_count = 0

        while fast:
            fast = fast.next
            f_count += 1
            if (f_count // 2 > s_count):
                slow = slow.next
                s_count += 1
        return slow