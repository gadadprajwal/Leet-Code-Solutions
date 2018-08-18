class Solution:
    def isPowerOfFour(self, num):
        
        # Each and every power of 4 has just one bit set in it and it has even number of zeros after the set bit
        # Down here in the program we have initially seen if the number has just one bit set
        # Once we know that the number has just one bit set we conclude that the number is power of 2
        # Now we have to find out weather there are even number of zeros after the set bit
        
        if num>0 and num & (num -1) == 0:
            res = 1  # For finding out weather the number of zeros are odd or even
            while num>0:
                num = num >> 1
                res = res ^ 1
            if res == 0:
                return True
        return False
        """
        :type num: int
        :rtype: bool
        """
        
