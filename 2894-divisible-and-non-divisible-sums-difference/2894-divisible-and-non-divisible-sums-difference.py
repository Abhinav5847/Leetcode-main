class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """

        divisible_m = 0
        not_divisible = 0

        for i in range(1,n+1):
            if i % m == 0:
                divisible_m += i
            else:
                not_divisible += i

        result =  not_divisible - divisible_m 

        return result            
        