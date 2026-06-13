class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = 1

        while True:

            if i % k == 0 and i not in nums:
                return i
            else:
                i += 1    


        