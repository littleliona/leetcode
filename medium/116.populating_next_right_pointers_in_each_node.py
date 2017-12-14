# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        #
        while root and root.left:
            next_level = root.left
            while root:
                root.left.next = root.right
                root.right.next = root.next and root.next.left
                root = root.next

            root = next_level
        #mine_method
        if not root:
            return 
        stack = [root]
        stack_child = []
        while stack:
            for i in range(len(stack)):
                node = stack.pop(0)
                if stack:
                    node.next = stack[0]
                else:
                    node.next = None
                if node.left:
                    stack_child.append(node.left)
                if node.right:
                    stack_child.append(node.right)

            stack = stack_child
            stack_child = []
        
s = Solution()
a = s.checkInclusion("ab","eidbaooo")
print(a)
