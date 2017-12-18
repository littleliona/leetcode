# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        dummpy_1 = pre_1 = ListNode(0)
        dummpy_2 = pre_2 = ListNode(1)

        current = head
        while current:
            if current.val < x:
                pre_1.next = current 
                pre_1 = pre_1.next 
                current = current.next
            else:
                pre_2.next = current
                pre_2 = pre_2.next
                current = current.next  
                
        pre_2.next = None
        pre_1.next = dummpy_2.next
        return dummpy_1.next


s = Solution()
root = ListNode(2)
root.next = ListNode(1)
a = s.partition(root,2)
