# recursion

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def md(root):
            if not root:
                return 0
            return 1 + max(md(root.left),md(root.right))
        return md(root)
      
      
      
      
 # bfs approach 

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        h = 0
        q = deque([root])
        while q:
            for i in range(len(q)):   # snapshot at current time
                temp = q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            h = h + 1
        return h
      
      
# iterative using stack to replicate the "stack"

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = [[root,1]]
        res = 1
        while stack:
            node, h = stack.pop()
            if node:
                res = max(res,h)
                stack.append([node.left,h+1])
                stack.append([node.right,h+1])
            
        return res
