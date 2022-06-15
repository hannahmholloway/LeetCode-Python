class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        
        arr.sort()
        
        diff = arr[1] - arr[0]
        
        for i in range(len(arr)-1):
            diff2 = arr[i+1] - arr[i]
            if diff2 != diff:
                return False
        return True
