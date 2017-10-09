# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        max_num = max(nums)
        index_max = nums.index(max_num)
        
        root = TreeNode(max_num)
        left_array = nums[:index_max]
        right_array = nums[index_max+1:]

        root.left = self.constructMaximumBinaryTree(left_array)
        root.right = self.constructMaximumBinaryTree(right_array)


        return root



s = Solution()
a = s.constructMaximumBinaryTree([3,2,1,6,0,5])
print(a)