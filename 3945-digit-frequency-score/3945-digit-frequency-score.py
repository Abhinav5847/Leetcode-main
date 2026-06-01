class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """

        num = str(n)

        og_list = []

        for i in num:
            og_list.append(int(i))

        print(og_list)    

        numbers = set(num)  

        li = list(numbers)

        last = [int(i) for i in li]

        res = 0

        for i in last:
            res += i * og_list.count(i)

        return res    

            
        