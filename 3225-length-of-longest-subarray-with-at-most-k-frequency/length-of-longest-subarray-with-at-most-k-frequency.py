class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        hm={}
        i=0
        ans=1
        for j,num in enumerate(nums):
            hm[num]=hm.get(num,0)+1
            while hm[num]>k:
                hm[nums[i]]-=1
                i+=1
            ans=max(ans,j-i+1)
        return ans
