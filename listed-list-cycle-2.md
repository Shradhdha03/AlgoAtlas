```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycleBruteForce(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        count=0
        while cur != None:
            if not hasattr(cur,'visited'):
                cur.visited = True
            else:
                return cur
            cur = cur.next
            count += 1
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != None and fast != None and slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
                
        return None
```