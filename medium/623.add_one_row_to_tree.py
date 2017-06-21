# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        #加根结点，原来的tree变为左结点
        if d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        #层次遍历
        #depth跟着一起入栈
        stack = []
        stack.append((root,1))
        while stack:
            temp = stack.pop()
            node = temp[0]
            depth = temp[1]
            if d-1 > depth:
                if node.right:
                    stack.append((node.right,depth+1))
                if node.left:
                    stack.append((node.left,depth+1))

            elif d-1 == depth:
                node_1 = TreeNode(v)
                node_2 = TreeNode(v)
                node_1.left = node.left
                node_2.right = node.right
                node.left = node_1
                node.right = node_2
            else:
                break

        return root

        
s = Solution()
a = s.addOneRow(4)
print(a)     

        

