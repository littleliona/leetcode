# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head

        previous,current,next_ = head,head.next,head.next.next

        head = current
        head.next = previous
        previous.next = self.swapPairs(next_)


        return head 
s = Solution()
a = s.lengthOfLIS()
print(a)
