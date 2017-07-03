# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next=None):
         self.val = x
         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        #two pointers
        odd = head
        even = even_ = head.next

        while odd.next and even.next:
            if odd.next.next:
                odd.next = odd.next.next
                odd = odd.next

            if even.next.next:
                even.next = even.next.next
                even = even.next

        odd.next = even_
        if even:
            even.next = None 
        return head
        


s = Solution()
a = s.oddEvenList(ListNode(1,ListNode(2,ListNode(3))))
print(a)     

        

