# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #层次遍历，利用队列
        #每一层输入结束后在末尾加上None
        #因为要找到最左边的叶子，所以右树先入列
        #mine--version1
        queue = []
        queue.append(root)
        queue.append(None)
        result = []
        tmp = []
        while queue:
            node = queue.pop(0)
            if node:
                tmp.append(node.val)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            else:
                result.append(tmp[-1])
                tmp = []
                if queue:
                    queue.append(None)  
        
        return result[-1]

        #mine--version2
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        
        return node.val

        #easy
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val



s = Solution()
a = s.findBottomLeftValue(TreeNode(1,TreeNode(2,TreeNode(4),None),TreeNode(3,TreeNode(5,TreeNode(7),None),TreeNode(6))))
print(a)
