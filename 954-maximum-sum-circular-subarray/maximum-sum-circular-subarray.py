class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=nums
        ts=0
        c_maxi=0
        c_mini=0
        maxsum=float('-inf')
        minsum=float('inf')
        for i in range(len(n)):
            ts+=n[i]
            c_maxi+=n[i]
            maxsum=max(maxsum,c_maxi)
            if c_maxi<0:
                c_maxi=0
            
            c_mini+=n[i]
            minsum=min(minsum,c_mini)
            if c_mini>0:
                c_mini=0
            
        if ts==minsum:
            return maxsum
        return max(ts-minsum,maxsum)
            