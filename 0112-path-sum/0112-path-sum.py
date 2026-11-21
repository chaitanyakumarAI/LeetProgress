# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if root==None:
            return False
        arr=[]
        s=0
        def findSum(s,root):
            s+=root.val
            if not root.left and not root.right:
                arr.append(s)
                
            if root.left:
                findSum(s,root.left)
            if root.right:
                findSum(s,root.right)
        findSum(s,root)
        return any(i==targetSum for i in arr)
