# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = pre = ListNode(0)

        node = root
        while node:
            pre.next = node.left
            if pre.next:
                pre = pre.next
            pre.next = node.right
            if pre.next:
                pre = pre.next

            node = node.next
            if not node:
                pre = dummy
                node = dummy.next
