class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        #mine
        if rowIndex == 0:
        	return [1]

        L = [1,1]
        res = []

        for i in range(1,rowIndex):
        	res.append(1)
        	for n in range(len(L)-1):
        		res.append(L[n]+L[n+1])
        	res.append(1)
        	L = res
        	res = []

        return L

        #easy 
        #zip(0,1,2,1)+(1,2,1,0) = (1,3,3,1)
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0]+row, row+[0])]
        return row

s = Solution()
a = s.getRow(4)
print(a)