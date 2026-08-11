class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n=len(nums)
        s=nums[0]
        for i in range(1,n):
            
            if nums[i]!=nums[i-1]+1:
                break
            else:
                s+=nums[i]
        while True:
            if s in nums:
                s+=1
            else:
                break
        return s
            