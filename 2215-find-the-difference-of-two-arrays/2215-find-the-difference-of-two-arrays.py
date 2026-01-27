class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        # list_one = []
        # for i in nums1:
        #     if i not in num2:
        li_one = set(nums1)
        li_two = set(nums2)

        res = li_one - li_two

        final = li_two - li_one

        li = []

        li.append(list(res))
        li.append(list(final))

        return li

        