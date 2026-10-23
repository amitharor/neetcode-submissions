'''
Input(s): root of binary tree
Output: diameter of tree

Constraints:
1 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100


Approach:
DFS (recursive)


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
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0


        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)


        dfs(root)
        return res
        