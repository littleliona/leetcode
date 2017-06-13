class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #h:从高到低，k：从低到高
        #相同的h，k小的在前面
        #排序结束后，同一高度的人的顺序是对的
        people.sort(key=lambda (h, k): (-h, k))

        #循环people
        #对于最高的人来说，其他人身高(均小于他)所在位置于他无关，他只在乎与他相同高度的人的位置，因此k即为他的索引值
        #同理对于身高第二高的人来说，他的位置仅与最高的人和身高相同的人有关，而这些人已经放入数组中了，所以k值即为索引值
        #以此类推
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue




      
s = Solution()
a = s.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])
print(a)
        

