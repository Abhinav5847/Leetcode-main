class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            if nums.count(i) == 2:
                res.append(i)

        final = set(res)

        return list(final)       
        