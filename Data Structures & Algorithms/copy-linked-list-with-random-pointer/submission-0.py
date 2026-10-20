'''
Input(s): head of a linked list that contains additional pointer, random that points to any other node in list or null
Output: deep copy of list

Constraints:
0 <= n <= 100
-100 <= Node.val <= 100
Node values are not guaranteed to be unique.
random is null or is pointing to some node in the linked list.

Approach:
init hash map that returns a new empty node whenever we access a key tht doesn't exist yet.
traverse the list
set the copied nodes vals
link its next pointer using the hash map
link its random pointer using the hash map

Time: O(n)
Space: O(n)
'''


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = defaultdict(lambda: Node(0))
        oldToCopy[None] = None

        curr = head
        while curr:
            oldToCopy[curr].val = curr.val
            oldToCopy[curr].next = oldToCopy[curr.next]
            oldToCopy[curr].random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]