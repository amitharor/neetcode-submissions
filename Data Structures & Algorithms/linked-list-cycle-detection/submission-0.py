'''
Input(s): beginning of a linked list: head
Output: bool; True is cycle in linked list; otherwise False

Constraints:
0 <= Length of the list <= 1000.
-1000 <= Node.val <= 1000
index is -1 or a valid index in the linked list.

Approach:
Fast and slow pointers
iterate through list
if the fast pointer reach back (cycles) to the same node as slow pointer; return true

otherwise return false


Time: O(n)
Space: O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        