# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import headq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = pre = ListNode(0)
        h = [(node.val,node) for node in lists if node]
        heapq.heapify(h)

        while h:
            value, node = h[0]
            if not node.next:
                heapq.heappop()
            else:
                heapq.heapreplace(node.next.val,node.next)

            pre.next = node
            pre = pre.next

        return dummy.next
        
s = Solution()
a = s.longestValidParentheses(')()())')
print(a)
