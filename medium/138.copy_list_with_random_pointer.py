# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        #method_fast
        dic = dict()
        m = n = head
        while m:
            dic[m] = RandomListNode(m.label)
            m = m.next
        while n:
            dic[n].next = dic.get(n.next)
            dic[n].random = dic.get(n.random)
            n = n.next
        return dic.get(head)

        #method O(n) O(1)
        if not head:
            return None
        
        pre = m = head
        while m:
            node = RandomListNode(m.label)
            m = m.next
            pre.next = node
            node.next = m
            pre = m

        m = head
        while m:
            if m.random:
                m.next.random = m.random.next
            m = m.next.next

        newhead = head.next
        pold = head
        pnew = newhead
        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew = pnew.next
        pold.next = None
        pnew.next = None
        return newhead


        #method_mine
        if not head:
            return None

        current = head
        pre = new_haad = RandomListNode(current.label)
        L = [new_haad]
        while current:
            if current.next:
                pre.next = RandomListNode(current.next.label)
                L.append(pre.next)
            if current.random:
                if current.random not in L:
                    pre.random = RandomListNode(current.random.label)
                else:
                    pre.random = L[L.index(current.random)]

            pre = pre.next
            current = current.next

        return new_haad 



s = Solution()
a = s.partition('aab')
print(a)
