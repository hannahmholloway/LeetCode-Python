class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        
        for i in nums:
            p *= i
            
        if p > 0:
            p = 1
        
        elif p == 0:
            p = 0
        
        elif p < 0:
            p = -1
            
        return p
            
