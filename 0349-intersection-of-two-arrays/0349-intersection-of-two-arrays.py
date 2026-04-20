class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # st_one = set(nums1)
        # st_two = set(nums2)

        # res = st_one.intersection(st_two)

        # fin = list(res) 
        # return fin 
        
        res = []
        for i in nums1:
            for j in nums2:
                if i == j:
                    res.append(i)
                    res.append(j)

        res = set(res)
        return list(res)          


        