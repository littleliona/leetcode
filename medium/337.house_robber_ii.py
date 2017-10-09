# Definition for a binary tree node.
from collections import defaultdict
class TreeNode(object):
     def __init__(self, x, left = None, right = None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.robDFS(root)[1]


    def robDFS(self,node):
        if node is None:
            return (0,0)     
        #[0] maximum money we can rob from subtree with node as root but without robbing node
        #[1] maximum money we can rob from subtree with node as root (may or may not rob node)
        #[0] = l[1] + r[1] (左右子树rob的最大值)
        #[1] = max(l[1] + r[1], l[0] + r[0] + node.val) 

        l = self.robDFS(node.left)
        r = self.robDFS(node.right)

        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))


s = Solution()
a = s.rob(TreeNode(4,TreeNode(1,TreeNode(2,TreeNode(3)))))
print(a)     

        

