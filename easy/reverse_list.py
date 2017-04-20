# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #mine
        if not head:
            return None
        if not head.next:
            return head
        p = head
        q = head.next
        if not q.next:
            p.next = None
            q.next = p
            return q
        else:
            r = head.next.next
            p.next = None
            q.next = p
            while r:
                p = q
                q = r
                r = r.next
                q.next = p
            return q
        #iterate
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev











s = Solution()
a = s.convertToBase7(-7)
print(a)