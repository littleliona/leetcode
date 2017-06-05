# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #利用队列，层次遍历
        q = deque()
        if root:
            q.append(root)
        result = []
        while q:
            result.append(float('-inf'))
            for _ in range(len(q)):
                top = q.popleft()
                result[-1] = max(result[-1], top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)
        return result

        
s = Solution()
a = s.largestValues(TreeNode(1,TreeNode(3,TreeNode(4),TreeNode(5)),TreeNode(2,TreeNode(5),TreeNode(4))))
print(a)



