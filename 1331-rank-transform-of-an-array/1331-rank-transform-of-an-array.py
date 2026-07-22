class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        sorted_arr = sorted(set(arr))

        numbers = {}

        for index,value in enumerate(sorted_arr):

            numbers[value] = index + 1

        res = []

        for i in arr:
            res.append(numbers[i])

        return res        
        
        # print(sorted_arr)
        # index_nums = []

        # for i in arr:

        #     index = sorted_arr.index(i) + 1

        #     index_nums.append(index)

        # return index_nums    
        






            

        