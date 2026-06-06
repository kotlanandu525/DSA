class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        tot=sum(nums)
        lsum=0
        rsum=0
        ans=[]
        for i in range(len(nums)):
            
            lsum+=nums[i]
            rsum=tot-lsum+nums[i]
            ans.append(abs(rsum-lsum))
        return ans