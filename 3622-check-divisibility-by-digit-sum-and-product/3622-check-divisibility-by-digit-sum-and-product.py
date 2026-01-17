class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        li = []
        for i in str(n):
            li.append(int(i))

        sum_li = 0
        plus_li = 1

        for i in li:
            plus_li *= i
            sum_li += i

        calc = sum_li + plus_li

        if n % calc  == 0:
            return True
        else:
            return False                

        