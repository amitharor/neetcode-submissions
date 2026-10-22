'''
Input(s): root of bianry tree
Output: root of inverted binar tree

Constraints:
0 <= The number of nodes in the tree <= 100.
-100 <= Node.val <= 100


Approach:
breadth first search


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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        return root