'''
Input(s): root of binary tree
Output: bool; return true if it's a valid binary search tree, otherwise False

Constraints:
1 <= The number of nodes in the tree <= 10000.
-1000000000 <= Node.val <= 1000000000

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
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, low, high):
            if not node:
                return True

            if not (low < node.val < high):
                return False
            
            return valid(node.left, low, node.val) and valid(node.right, node.val, high)

        return valid(root, float('-infinity'), float('infinity'))