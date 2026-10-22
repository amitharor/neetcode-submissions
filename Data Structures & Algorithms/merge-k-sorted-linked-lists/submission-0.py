class ListNode:
    def __init__ (self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        heap = []
        dummy = ListNode() 
        tail = dummy

        # iterate through every list head
        for listIndex, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, listIndex, node))

        # repeated choosing the smallest avail val
        while heap:
            value, listIndex, node = heapq.heappop(heap) #get minimum
            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(heap, (node.next.val, listIndex, node.next))

        return dummy.next
