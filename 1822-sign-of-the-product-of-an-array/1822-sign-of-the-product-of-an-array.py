class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 1

        for i in nums:
            res *= i

        if res > 0:
            return 1
        elif res < 0:
            return -1
        else:
            return 0            
        