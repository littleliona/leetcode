
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        #mine -- dfs and stack
        #stack -- (node,sum to the current node(including current node))
        if not root:
            return False
            
        stack = []
        stack.append((root,root.val))

        while stack:
            x = stack.pop()
            node = x[0]
            if node.right:
                stack.append((node.right,x[1]+node.right.val))

            if node.left:
                stack.append((node.left,x[1]+node.left.val))

            if not node.left and not node.right:
                if x[1] == target:
                    return True

        return False

        #recursive
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

       
s = Solution()
a = s.hasPathSum(TreeNode(1),1)
print(a)