class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """

        for i in target:
            if target.count(i) != arr.count(i):
                return False
        return True               

        