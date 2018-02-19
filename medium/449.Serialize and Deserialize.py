# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = list()

        def pre_order(node):
            if node:
                vals.append(str(node.val))
                pre_order(node.left)
                pre_order(node.right)

            else:
                return
        pre_order(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(int(val) for val in data.split())

        def build(minVal,maxVal):
            if vals and minVal < vals[0] < maxVal:
                val = vals.popleft()
                node = TreeNode(val)
                node.left = build(minVal,val)
                node.right = build(val,maxVal)
                return node
            return None

        return build(float('-inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    str_num = int(raw_input())
    for i in range(str_num):
        string = raw_input()
        print longest_palindrome(string)

    

