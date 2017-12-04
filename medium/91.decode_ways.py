class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #w tells the number of ways
        #v tells the previous number of ways
        #d is the current digit
        #p is the previous digit
        v, w, p = 0, int(s>''), ''
        for d in s:
            v, w, p = w, (d>'0')*w + (9<int(p+d)<27)*v, d
        return w

        # dp[i] += dp[i-1] if current number > 0
        # dp[i] += dp[i-2] if 9 < current number + previous number < 27
        if not s:
            return 0

        V = len(s)
        dp = [0 for i in range(V+1)]
        dp[0] = 1

        if int(s[0]) > 0:
            dp[1] = 1
        else:
            return 0

        for i in range(2,V+1):
            if int(s[i-1]) > 0:
                dp[i] += dp[i-1]
            if 9 < int(s[i-2]+s[i-1]) <= 26:
                dp[i] += dp[i-2]
            

        return dp[V]
                
s = Solution()
a = s.numDecodings("17")
print(a)
