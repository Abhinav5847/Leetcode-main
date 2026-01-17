class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        res = []

        for i in range(1,a+1):
            if a % i == 0 and b % i == 0:
                res.append(i)

        return len(res)         
        