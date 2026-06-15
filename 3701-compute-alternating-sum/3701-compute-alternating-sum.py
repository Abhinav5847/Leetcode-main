class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        odd = 0
        even = 0

        for i in range(len(nums)):

            if i % 2 == 0:
                even -= nums[i]
            else:
                odd -= nums[i]

        return abs(even) - abs(odd)                