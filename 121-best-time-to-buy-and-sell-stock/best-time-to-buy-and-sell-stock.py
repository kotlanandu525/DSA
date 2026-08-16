class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini=float('inf')
        ans=0
        for p in prices:
            mini=min(p,mini)
            ans=max(ans,p-mini)

        return ans