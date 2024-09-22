# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
    # SOLUTION #1: Unoptimized but straightforward
    # SC = O(N); TC = O(N)
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ll = deque()
        # while head:
        #     ll.appendleft(head)
        #     head = head.next
        # for i,node in enumerate(ll):
        #     if i+1 < len(ll):
        #         node.next = ll[i+1]
        #     else:
        #         node.next = None
        # return ll[0] if len(ll) > 0 else None
    
    # SOLUTION #2: Optimized two-pointer, no extra memory
    # SC = O(1); TC = O(N)
        prev, current = None, head
        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev


    