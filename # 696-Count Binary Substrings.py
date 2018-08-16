class Solution(object):
    def countBinarySubstrings(self, s):
        sum_ = 0
        # Group will store the count of consequtive 1s and 0s.
        
        # 0(0 1) group will have [2, 1] possible pair is only one since there is only one 1.
        group = [1]
        
        
        for i in xrange(1,len(s)):
            if s[i-1] != s[i]:
                group.append(1)
            else:
                group[-1] += 1
        
        # Since the minimum requiremnent will only be fullfilled if we could manage to have exactly one 1 with corresponding 0.
        for i in range(0,len(group)-1):
            sum_ += min(group[i],group[i+1])
            
        return sum_
        
        
        """
        :type s: str
        :rtype: int
        """
        
