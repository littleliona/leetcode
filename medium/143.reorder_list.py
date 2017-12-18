# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #method_1
        if not head or not head.next:
            return
        a, b = self._splitList(head)
        b = self._revereList(b)
        head = self._mergeLists(a, b)

        #method_mine
        if not head or not head.next or not head.next.next:
            return

        slow, fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow.next
        stack = []
        current = mid.next 
        while current:
            stack.append(current)
            current = current.next

        mid.next = None
        while head:
            if stack:
                node = stack.pop()
                node.next = head.next
                head.next = node
                head = head.next.next
            else:
                break
        

    def _splitList(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        middle = slow.next
        slow.next = None
        return head, middle
    def _revereList(self, head):
        last = None
        currentNode = head
        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode
        return last
    def _mergeLists(self, a, b):
        tail = a
        head = a
        a = a.next
        while b:
            tail.next = b
            tail = tail.next
            b = b.next
            if a:
                a, b = b, a
        return head
            

s = Solution()
a = s.partition('aab')
print(a)
