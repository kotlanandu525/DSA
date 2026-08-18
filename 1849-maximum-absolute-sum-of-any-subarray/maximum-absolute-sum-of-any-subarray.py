class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s=0
        minsum=float('inf')
        maxsum=float('-inf')
        for num in nums:
            s+=num
            if s<0:
                s=0
            maxsum=max(s,maxsum)
        s=0
        for num in nums:
            s+=num
            if s>0:
                s=0
            minsum=min(s,minsum)
            
        return max(abs(minsum),abs(maxsum))
        