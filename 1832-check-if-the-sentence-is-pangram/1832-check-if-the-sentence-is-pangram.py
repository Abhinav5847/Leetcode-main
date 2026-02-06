class Solution(object):
    def checkIfPangram(self, sentence):
        a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        res = set(sentence)

        if len(res) == len(a):
            return True
        else:
            return False    


        """
        :type sentence: str
        :rtype: bool
        """
        