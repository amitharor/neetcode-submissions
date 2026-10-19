'''
Input(s): head of singly linked list
Output: reverse list and return the new beginning

Constraints:
0 <= The length of the list <= 1000.
-1000 <= Node.val <= 1000

Approach:


Time: O(n)
Space: O(1)
'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

        