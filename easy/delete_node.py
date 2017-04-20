# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next_=None):
         self.val = x
         self.next = next_

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


s = Solution()
node = ListNode(1,ListNode(2,ListNode(3,ListNode(4))))
s.deleteNode(node.next)