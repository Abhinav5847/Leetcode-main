class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []

        for i in nums:
            if nums.count(i) == 1:
                res.append(i)

        return res