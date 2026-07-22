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

        print(numbers)

        for i in arr:
            res.append(numbers[i])

        return res        
        
   
        






            

        