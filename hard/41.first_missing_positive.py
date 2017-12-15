class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(A)==0:  
            return 1  
        i=0  
        while i<len(A):  
            if A[i]<=len(A) and A[i]>0 and A[A[i]-1]!=A[i]:  
                A[A[i] - 1] , A[i] = A[i], A[A[i] - 1] 
            else:
                i+=1  
        i=0          
        while i<len(A):  
            if A[i]!=i+1:  
                return i+1  
            i+=1  
        return len(A)+1  
