class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        freq=[0]*(max(nums)+1)
        for i in nums:
            freq[i]+=i

        dp=[0]*len(freq)
        dp[1]=freq[1]
        for i in range(2,len(freq)):
            dp[i]=max(dp[i-1],freq[i]+dp[i-2])
        
        return dp[len(freq)-1]
