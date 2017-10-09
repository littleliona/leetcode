# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #short
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])            
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans

        #mine
        if not root:
            return []

        res = []
        stack = [(root,1)]
        depth = 1
        ans = []

        while stack:
            x = stack.pop(0)
            node = x[0]
            if depth != x[1]:
                res.append(ans)
                ans = []
                ans.append(node.val)
                depth = x[1]
            else:
                ans.append(node.val)

            if node.left:
                stack.append((node.left,x[1]+1))
            if node.right:
                stack.append((node.right,x[1]+1))
        
        res.append(ans)
        return res
        




s = Solution()
a = s.longestPalindromeSubseq("cbbd")
print(a)     

        

