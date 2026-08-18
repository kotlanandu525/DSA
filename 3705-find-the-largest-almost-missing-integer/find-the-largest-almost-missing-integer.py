class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)
        f=Counter(nums)
        
        
        
        if k==1:
            ss=[x for x,v in f.items() if v==1]
            return max(ss) if ss else -1
        

        a=nums[0]
        b=nums[n-1]
        if a==b:
            return -1
        if f[a]==1 and f[b]==1:
            return max(a,b)
        
        else:
            if f[a]!=1 and f[b]==1:
                return b
            elif f[b]!=1 and f[a]==1:
                return a
            else:
                return -1

        