class Solution(object):
    def rob(self, nums):
        
        
        l = len(nums)
        
        if l == 0:
            return 0
        
        if l == 1:
            return nums[0]
        
        out = []
        
        for i in range(0,l):
            out.append(0)
        
        out[0] = nums[0]
        out[1] = max(nums[1],nums[0])        
        
        # DP formula
        for i in range(2,l):
            out[i] = max(out[i-2]+nums[i],out[i-1])
        
        # Return the last element from the DP list
        return out[l-1]
            
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
