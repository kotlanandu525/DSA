class Solution:
    


    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[]
        def binary(res,n):
            l=0
            r=len(res)-1
        
            while l<=r:
                mid=(l+r)//2
                if res[mid]==n:
                    return mid
                elif res[mid]<n:
                    l=mid+1
                else:
                    r=mid-1
            return l
        for num in nums:
            if not res or res[-1]<num:
                res.append(num)
            else:
                idx=binary(res,num)
                res[idx]=num
        return len(res)