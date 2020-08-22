class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        pre_pos = -1
        
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            
            if pre_pos != -1:
                
                if (i-pre_pos-1) < k:
                    return False
                
            pre_pos = i
        
        
        return True
