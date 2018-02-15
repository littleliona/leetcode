# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            res.append(str(node.val) if node else '#')
            if node:
                queue += node.left, node.right
        
        return ','.join(res)     

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodes = [TreeNode(v) if v != '#' else None for v in data.split(',')]
        if not nodes:
            return None
        nodesIter = iter(nodes)
        queue = deque([next(nodesIter)])
        while queue:
            node = queue.popleft()
            if not node:
                continue
            node.left = next(nodesIter)
            node.right = next(nodesIter)
            if node:
                queue += node.left, node.right
        return nodes[0]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


        


if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(codec.serialize(root))