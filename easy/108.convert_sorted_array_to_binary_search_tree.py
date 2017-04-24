# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sortedArrayTo(self, nums, start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayTo(nums,start,mid-1)
        root.right = self.sortedArrayTo(nums,mid+1,end)
        return root
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #mine
        return self.sortedArrayTo(nums,0,len(nums)-1)
        #easy
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

    
s = Solution()
a = s.sortedArrayToBST([1,2,3,4,5])
print(a)