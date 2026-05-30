class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        hold = 1000
        if n < 1000:
            return 0

        num = n - hold + 1

        return num  


        