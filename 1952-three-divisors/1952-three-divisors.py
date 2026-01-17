class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = []

        for i in range(1,n+1):
            if n % i == 0:
                res.append(i)
        if len(res) == 3:
            return True
        else:
            return False            
        