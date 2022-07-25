# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque()
        q.append(root)
        res = []
        while(q):
            qlen = len(q)
            clist = []
            for i in range(qlen):
                
                curr = q.popleft()
                if not curr:
                    continue
                clist.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
            if clist:
                res.append(clist)
        return res
