# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
            if root==None:
                return None
            root.left,root.right=root.right,root.left
            invertTree(root.left)
            invertTree(root.right)
            return root
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if (p==None and q==None):
                return True
            if(p==None or q==None or p.val!=q.val):
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        inverted_right = invertTree(root.right)
        return isSameTree(root.left, inverted_right)
        