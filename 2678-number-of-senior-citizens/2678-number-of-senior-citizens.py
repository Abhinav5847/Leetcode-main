class Solution(object):
    def countSeniors(self, details):
        """
        :type details: List[str]
        :rtype: int
        """

        c = 0

        for i in details:

            res = i[11:13]

            if int(res) > 60:

                c += 1

        return c        



                

            
        