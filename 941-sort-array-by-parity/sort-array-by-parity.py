class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        if n<=1:
            return nums
        l=0
        for i in range(n):
            if nums[i]%2==0:
                nums[l],nums[i]=nums[i],nums[l]
                l+=1
        return nums
        
