# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x, next_):
         self.val = x
         self.next = next_

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        node = root
        length = 0
        L = []
        while node != None:
            length += 1
            node = node.next

        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)

        # Split up the list
        previous, current = None, root
        for index, num in enumerate(res):
            if previous:
                previous.next = None

            res[index] = current

            for i in range(num):
                previous , current = current, current.next

        return res


s = Solution()
a = s.splitListToParts(ListNode(1,ListNode(2,ListNode(3,None))),4)
for node in a:
    if node:
        print(node.val)
    else:
        print('1')



