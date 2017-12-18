class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        p = r = previous = None
        i = 0
        reverse_before = reverse_head = reverse_after = None 

        current = head
        while current:
            i += 1
            if i == m:
                reverse_before = previous 
                p = reverse_head = current 
                current = current.next

            elif i > m and i < n:
                r = current
                current = current.next
                r.next = p
                p = r

            elif i == n:
                reverse_after = current.next
                current.next = p
                break 

            else:
                previous = current 
                current = current.next
        
        if reverse_before:
            reverse_before.next = current
            reverse_head.next = reverse_after 

        else:
            head = current
            reverse_head.next = reverse_after

        return head

        
