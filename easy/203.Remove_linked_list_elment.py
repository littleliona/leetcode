# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        while head.val == val:
            head = head.next
        
        pre = current = head
        while current:
            if current.val == val:
                pre.next = current.next
                current = current.next
            else:
                pre = current
                current = current.next

        return head

        
        

        
s = Solution()
a = s.twoSum()
print(a)