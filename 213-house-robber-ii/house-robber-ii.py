class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        dp = [0] * (n-1)
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n-1):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
     
        ap=[0]*(n-1)
        ap[0]=nums[1]
        ap[1]=max(nums[1],nums[2])
        for i in range(2, n-1):
            ap[i] = max(ap[i-1], nums[i+1] + ap[i-2])
        return max(dp[-1],ap[-1]) 