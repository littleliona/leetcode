# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #mine
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack[::-1] == stack

        #find the middle and reverse the first half
        #compare with the second half
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return not rev  

        
        

        
s = Solution()
a = s.twoSum()
print(a)