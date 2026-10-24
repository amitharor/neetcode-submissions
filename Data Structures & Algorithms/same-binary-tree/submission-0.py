'''
Input(s): roots of two binary trees
Output: bool; return True if the tree are equivalent; otherwise False

Constraints:
0 <= The number of nodes in both trees <= 100.
-100 <= Node.val <= 100


Approach:
DFS


Time: O(n)
Space: O(h)
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False