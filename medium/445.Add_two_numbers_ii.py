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
        #not reverse the linked list
        #using stack
        #头插法创建链表
        stack1 = []
        stack2 = []
        carry = 0
        head = None
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        while stack1 or stack2 or carry!=0:
            v1 = stack1.pop() if stack1 else 0
            v2 = stack2.pop() if stack2 else 0
            node = ListNode((v1 + v2 + carry) % 10)
            carry = (v1 + v2 + carry) / 10
            node.next = head
            head = node

        return head



        #reverse_linked_list
        #mine--easy version
        #选定reverse_l1作为相加后的list
        reverse_l1 = self.reverse_list(l1)
        reverse_l2 = self.reverse_list(l2)

        carry = 0
        pre_node = head = reverse_l1

        while reverse_l2 or reverse_l1 or carry!=0:
            v1 = 0 if reverse_l1 == None else reverse_l1.val
            v2 = 0 if reverse_l2 == None else reverse_l2.val
            if not reverse_l1:
                reverse_l1 = ListNode((v1 + v2 + carry) % 10)
                pre_node.next = reverse_l1
            else:
                reverse_l1.val = (v1 + v2 + carry) % 10

            
            carry = (v1 + v2 + carry) / 10
            pre_node = reverse_l1
            reverse_l2 = reverse_l2.next if reverse_l2 else None
            reverse_l1 = reverse_l1.next if reverse_l1 else None



        return self.reverse_list(head)
    
    def reverse_list(self, head):
        """
        :type head:ListNode
        :rtype: ListNode
        """
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
        
        
s = Solution()
a = s.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))),ListNode(5,ListNode(6,ListNode(4))))
print(a)
