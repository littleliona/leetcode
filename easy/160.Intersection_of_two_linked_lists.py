# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        #idea -- assume list A length is L1, B length is L2 and L1<L2
        #pa first hit A's end,and is assigned to headB,now the length left is L2
        #when pa hit A's end ,pb's left length is L2-L1,let pb traverse A when it hit the end,and now the left length for pb is L2-L1+L1 == L2
        #because pa's length == pb's length, we can find that if they meet or both hit the end
        pa,pb = headA,headB
        while pa is not pb:
            # if either pointer hits the end, switch head and continue the second traversal, 
            # if not hit the end, just move on to next
            pa = headB if pa == None else pa.next
            pb = headA if pb == None else pb.next

        return pa # only 2 ways to get out of the loop, they meet or the both hit the end=None


        
        

        
s = Solution()
a = s.twoSum()
print(a)