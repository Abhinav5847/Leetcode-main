class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current = 0
        max_num = 0

        for i in nums:

            if i == 1:
                current += 1
            else:
                current = 0

            max_num = max(current,max_num)

        return max_num        
        
