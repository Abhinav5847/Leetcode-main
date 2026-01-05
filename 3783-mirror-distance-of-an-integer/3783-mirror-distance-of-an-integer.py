class Solution(object):
    def mirrorDistance(self, n):
        res = str(n)
        fin = res[::-1]
        num = int(fin)
        last = num - n

        return abs(last)
        """
        :type n: int
        :rtype: int
        """
        