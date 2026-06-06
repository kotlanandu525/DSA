class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n=len(nums)     
        lsum=[0]*n
        rsum=[0]*n
        ans=[0]*n
        for i in range(1,len(nums)):
            
            lsum[i]=lsum[i-1]+nums[i-1]
        for i in range(len(nums)-2,-1,-1):

            rsum[i]=rsum[i+1]+nums[i+1]
        for i in range(len(nums)):
            ans[i]=abs(rsum[i]-lsum[i])
        return ans