'''
Input(s): root of a binary tree and k (int)
Output: kth smallest val in tree

Constraints:
1 <= k <= The number of nodes in the tree <= 10,000.
0 <= Node.val <= 10,000


Approach:
in order traversal


Time: O(n)
Space: O(n)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)

        inorder(root)
        return values[k-1]