# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        current = head

        while current and current.next:
            value = current.next.val
            if current.val < value:
                current = current.next
                continue
            
            if p.next.val > value:
                p = dummy

            while p.next.val < val:
                p = p.next

            new = current.next
            current.next = new.next 
            new.next = p.next 
            p.next = new 

        return dummy.next 

s = Solution()
a = s.partition('aab')
print(a)
