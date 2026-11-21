# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        if root==None:
            return []
        res=[]
        s=0
        def findSum(s,root,dup):
            s+=root.val
            dup.append(root.val)
            if not root.left and not root.right:
                if s==targetSum:
                    res.append(dup.copy())
            if root.left:
                findSum(s,root.left,dup)
            if root.right:
                findSum(s,root.right,dup)
            dup.pop()
        findSum(s,root,[])
        return res