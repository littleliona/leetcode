# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #method_list
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        temp = slow.next
        slow.next = None
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next)

        return root
        #method_array
        L = []
        while head:
            L.append(head.val)
            head = head.next
        
        return self.sortedArrayToBST(num)
    
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2
        root = TreeNode(num[mid]) 

        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:]) 

        return root 
