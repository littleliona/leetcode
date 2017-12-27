# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #method
        if head is None or k <= 1:
            return head
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        count = 0
        cur = head
        while cur != None:
            count += 1
            cur = cur.next # cur is the first node in next round
            if count == k:
                prev = self.reverse(prev, cur) # prev points to the node before cur
                count = 0
        return dummy.next
    
    def reverse(self, prev, end): # Exclusive
        cur = prev.next # inclusive starat
        while cur.next != end: 
            next = cur.next
            cur.next = next.next
            next.next = prev.next
            prev.next = next
        return cur # return the node before end
        #method_mine

        dummy = pre = ListNode(0)
        if k == 0 or k == 1:
            return head

        count = 0
        start, end, rev_end, rev_head = None, None, None, None
        dummy.next = head
        while head:
            if count == 0:
                start = head
                count += 1
                head = head.next
            else:
                count += 1
                if count == k:
                    end = head
                    head = head.next
                    end.next = None
                    rev_head, rev_end = self.reverse(start, end)
                    pre.next = rev_head
                    pre = rev_end
                    pre.next = head
                    count = 0
                else:
                    head = head.next
            

        return dummy.next
    def reverse(self, head, end):
        pre = None

        rev_end = current = head 
        while current:
            p = current 
            current = current.next
            p.next = pre
            pre = p

        return (pre,rev_end)  


s = Solution()
head = ListNode(1)
head.next = ListNode(2)
a = s.reverseKGroup(head, 2)
print(a)
