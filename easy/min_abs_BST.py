# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x, left=None, right=None):
         self.val = x
         self.left = left
         self.right = right

class Solution(object):
    def getMinimumDifference(self, root):
        nums = self.inorder(root)
        return min(nums[i+1]-nums[i] for i in range(len(nums)-1))
        
    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []
		


	

s = Solution()
a = s.getMinimumDifference(TreeNode(5,TreeNode(3,TreeNode(2),TreeNode(5)),TreeNode(7,None,TreeNode(8))))
print(a)