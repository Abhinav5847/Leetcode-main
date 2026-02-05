class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = 0
        st = ""
        for i in nums:
            res += i
            st += str(i)
        
        digi = 0
        for i in st:
            digi += int(i)

        final = res - digi

        return final

        