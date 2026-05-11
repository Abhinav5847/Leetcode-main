class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        res = [str(i) for i in nums]

        joined = "".join(res)

        last = []

        for i in joined:
            last.append(int(i))

        return last
