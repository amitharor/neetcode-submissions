'''
Input(s): head of linked list, and n (int)
Output: remove nth node from head and return it's head

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz


Approach:
init dummy node
init left/right pointers

increment right pointer "n" times
iterate while right pointer is not null
increment left and right pointers
once the right pointer becomes null, left pointer can be set to left.next.next (to remove the nth node)
return dummy's next


Time: O(n)
Space: O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        for _ in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next