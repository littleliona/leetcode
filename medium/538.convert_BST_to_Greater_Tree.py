# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # main idea : 倒叙遍历树，然后加value更新每个结点val的值
        myStack = []
        node = root
        value = 0
        while node or myStack:
            while node:
            # 从根节点开始，一直找它的右子树
                myStack.append(node)
                node = node.right
        # while结束表示当前节点node为空，即前一个节点没有右子树了
            node = myStack.pop()
            x = node.val
            node.val += value
            value += x
        # 开始查看它的左子树
            node = node.left
        return root

        
s = Solution()
a = s.convertBST(TreeNode(2,TreeNode(0,TreeNode(-4),TreeNode(1)),TreeNode(3)))
print(a)
