# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_sub_root(first, second):
            if not first and not second:
                return True
            
            if not first or not second or first.val != second.val:
                return False
            
            return is_sub_root(first.left, second.left) and is_sub_root(first.right, second.right)
        
        if not root:
            return 

        if root.val == subRoot.val:
            if is_sub_root(root, subRoot):
                return True

        if self.isSubtree(root.left, subRoot):
            return True

        if self.isSubtree(root.right, subRoot):
            return True

        return False
        
