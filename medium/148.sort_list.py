# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        pre = None 
        slow = fast = head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        l = self.sortList(head)
        r = self.sortList(slow)

        return self.merge(l,r)
    
    def merge(self, h1, h2):
        dummy = pre = ListNode(0)

        while h1 and h2:
            if h1.val < h2.val:
                pre.next = h1
                pre = h1
                h1 = h1.next
            else:
                pre.next = h2
                pre = h2
                h2 = h2.next

        pre.next = h1 or h2

        return dummy.next
s = Solution()
a = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(a)
