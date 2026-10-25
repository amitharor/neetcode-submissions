'''
Input(s): root of binary tree
Output: return list of vals that are visible from the right side of tree

Constraints:
0 <= number of nodes in the tree <= 100
-100 <= Node.val <= 100

Approach:
using BFS, we can get the last element of each level
return results

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        if not root:
            return result

        queue = deque([root])
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()

                if i == levelSize - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result