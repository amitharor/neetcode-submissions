'''
Input(s): head of singly linked list
Output: return nodes reorder (0, n-1, 1, n-2, 2, n-3... etc)

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000

Approach:
use slow and fast pointer
find the middle of linked list

reverse second half of list
merge alternating


Time: O(n)
Space: O(1)
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # 1 find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2 reverse second half
        second = slow.next
        slow.next = None
        prev = None
        
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # 3 merge alternating
        first, second = head, prev
        while second:
            first_next, second_next = first.next, second.next
            first.next = second
            second.next = first_next
            first, second = first_next, second_next