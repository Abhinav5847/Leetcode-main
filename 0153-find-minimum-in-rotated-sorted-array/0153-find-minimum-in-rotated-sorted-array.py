class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums)
        res = nums[0]
        for i in nums:
            if i < res:
                res = i
        return res        
        