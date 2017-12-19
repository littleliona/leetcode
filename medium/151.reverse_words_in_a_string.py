# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #method_
        word = ""
        words = ""
        s = s[::-1]
        for j, i in enumerate(s):
            # character is not space, a current word exists, 
            # and previous character is space, e.g. i=b in " a b":
            if i != " " and word != "" and s[j-1] == " ":
                # add current word to words and append " " to later add this i
                words += (word + " ")
                word = i
            # character is not space, but it's either first character in string
            # or is part of current word, e.g. i=b in "b", " b" "ab", "a ab "
            elif i != " ":
                word = i + word
            else:
                continue

        words += word
        
        return(words)

        #one_line
        L = s.split()
        return ' '.join(L[::-1])


s = Solution()
a = s.partition('aab')
print(a)
