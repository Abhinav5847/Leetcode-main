class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        
        # a = original
        # for i in nums:
        #     if a in nums:
        #         a *= 2
        #     else:
        #         return a

        i = True
        a = original
        while i:
            if a in nums:
                a *= 2
            else:
                i = False

        return a            

               

        