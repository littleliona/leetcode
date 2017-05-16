class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        #mine
        n = str(bin(n))[2:]
        n = n[::-1]
        if len(n) < 32:
            n += (32-len(n))*'0'

        return int(n,2)

        #same idea
        #use of format
        #032b-- 0 means padding char, 32b means 32 bits binary
        #:后面带要填充的字符，只能是一个字符，默认为空格
        

        oribin='{0:032b}'.format(n)
        reversebin=oribin[::-1]
        return int(reversebin,2)







s = Solution()
a = s.reverseBits(43261596)
print(a)
    


        





