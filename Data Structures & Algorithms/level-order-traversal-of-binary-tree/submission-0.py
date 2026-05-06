# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        ans = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            curr_level = [queue.popleft() for _ in range(level_size)]
            ans.append([node.val for node in curr_level if node])

            for i in range(level_size):
                curr = curr_level[i]
                if curr:
                    if curr.left:
                        queue.append(curr.left)
            
                    if curr.right:
                        queue.append(curr.right)
        
        return ans