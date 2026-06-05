class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans=0
        f={}
        for x in nums:
            f[x]=f.get(x,0)+1
        for x in f:
            if x+1 in f:
                ans=max(ans,f[x]+f[x+1])
        return ans