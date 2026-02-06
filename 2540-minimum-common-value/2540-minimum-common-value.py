class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # res = []
        # for i in nums1:
        #     for j in nums2:
        #         if i == j:
        #             res.append(i)
        # return min(res)
        li_one = set(nums1)
        li_two = set(nums2)

        res = li_one & li_two

        li = list(res)

        if len(li) == 0:
            return -1
        else:
            return min(li)    

        