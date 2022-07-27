# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        currSum = 0
        def travel(node):
            if not node:
                return
            nonlocal currSum
            travel(node.right)
            current = node.val
            node.val = node.val + currSum
            currSum = current + currSum
            
            travel(node.left)
        travel(root)
        return root
