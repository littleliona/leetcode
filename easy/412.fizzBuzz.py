class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        #mine
        L = []
        for i in range(1, n+1):
        	if i%15 == 0:
        		L.append("FizzBuzz")
        	elif i%3 == 0:
        		L.append("Fizz")
        	elif i%5 == 0:
        		L.append("Buzz")
        	else:
        		L.append(str(i))
        return L

        #easy
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]


s = Solution()
s.fizzBuzz(15)
