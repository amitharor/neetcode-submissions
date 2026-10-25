'''
Input(s): binary tree root
Output: return list of sublist of vals at each level

Constraints:
0 <= The number of nodes in the tree <= 2000.
-1000 <= Node.val <= 1000

Approach:
use BFS to go level by level and push elements from each level into results list

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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if not root:
            return result

        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                # print(f'elements in this level: {len(queue)}')
                node = queue.popleft()
                # print(f'node val: {node.val}')
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)
            
        return result