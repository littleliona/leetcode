# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        add = 0
        head = previous = ListNode(0)
        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + add
            elif l1:
                value = l1.val + add
            elif l2:
                value = l2.val + add
            
            if value  < 10: 
                current = ListNode(value)
                add = 0
            else:
                current = ListNode(value - 10)
                add = 1
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            previous.next = current
            previous = current 
            
        if add:
            current = ListNode(add)
            previous.next = current
        
        current.next = None
        return head.next 
s = Solution()
a = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(a)
