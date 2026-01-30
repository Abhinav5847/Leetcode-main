class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        min_i = min(nums)
        max_i = max(nums)

        res = []

        for i in range(min_i,max_i + 1):
            res.append(i)
        
        final = []
        for i in res:
            if i not in nums:
                final.append(i)
        return final            
                    

        