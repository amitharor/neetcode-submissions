'''
Input(s): root of a binary tree
Output: num of GOOD nodes within tree

Constraints:
1 <= number of nodes in the tree <= 100,000
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
    def goodNodes(self, root):
        def count(node, max_so_far):
            if not node:
                return 0
            
            good = 1 if node.val >= max_so_far else 0
            new_max = max(max_so_far, node.val)
            return good + count(node.left, new_max) + count(node.right, new_max)

        return count(root, root.val)