# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #
        current = head
        storeList = []
        while current != None:
            storeList.append(current)
            current = current.next
        if len(storeList) <= 1:
            return head
        k = k % len(storeList)
        if k == 0:
            return head
        res = storeList[-k]
        storeList[-k - 1].next = None
        storeList[-1].next = head
        return res

        #mine
        if not head or not head.next or k == 0:
            return head 
        
        length_list = 1
        current = head 
        while current.next:
            current = current.next
            length_list += 1
        
        current.next = head
        
        current = head 
        for i in range(1,length_list - (k % length_list)):
            current = current.next

        head = current.next
        current.next = None

        return head

s = Solution() 
a = s.threeSum([-1,0,1,2,-1,-4])
print(a)

