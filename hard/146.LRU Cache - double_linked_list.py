from collections import OrderedDict 
class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.value = v
        self.pre = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic:
            return -1

        n = self.dic[key]
        self._remove(n)
        self._add(n)
        
        return n.value
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            self._remove(self.dic[key])
        n = Node(key,value)
        self._add(n)
        self.dic[key] = n

        if len(self.dic) > self.capacity:
            n = self.head.next
            self._remove(n)
            del self.dic[n.key]

    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

    def _add(self, node):
        p = self.tail.pre
        p.next = node
        node.pre = p
        node.next = self.tail
        self.tail.pre = node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

s = Solution()
a = s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
print(a)
