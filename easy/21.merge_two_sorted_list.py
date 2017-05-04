# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next_ = None):
         self.val = x
         self.next = next_

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #mine
        if not l1:
            return l2
        if not l2:
            return l1

        head = prev1 = l1
        prev2 = l2
    
        while l1 and l2:
            if l1.val <= l2.val:
                prev1 = l1
                l1 = l1.next
            else:
                if prev1 == l1:
                    l2 = l2.next
                    prev2.next = prev1
                    prev1 = prev2
                    prev2 = l2
                    head = prev1
                else:
                    l2 = l2.next
                    prev1.next = prev2
                    prev2.next = l1
                    prev1 = prev1.next
                    prev2 = l2

        if l2:
            prev1.next = l2

        return head
        #easy
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next



s = Solution()
a = s.mergeTwoLists(ListNode(2),ListNode(1))
print(a)