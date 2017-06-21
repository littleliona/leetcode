# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        #length is known and fixed
        self.L = []
        while head:
            self.L.append(head.val)
            head = head.next

        #length is unknown and dynamically changed
        self.head = head
        
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.sample(self.L,1)

        # reservoir sampling
        # 蓄水池算法
        result, node, index = self.head, self.head.next, 1
        while node:
            if random.randint(0, index) is 0:
                result = node
            node = node.next
            index += 1
        return result.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()       

        

