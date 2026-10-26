'''
Input(s): root of non empty binary tree
Output: return max path sum of any non-empty path

Constraints:
1 <= The number of nodes in the tree <= 30000.
-1000 <= Node.val <= 1000


Approach:
DFS


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
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val

        def gain(node):
            if not node:
                return 0

            leftGain = max(gain(node.left), 0) #drop negatives
            rightGain = max(gain(node.right), 0)

            self.best = max(self.best, node.val + leftGain + rightGain)
            return node.val + max(leftGain, rightGain)

        gain(root)
        return self.best