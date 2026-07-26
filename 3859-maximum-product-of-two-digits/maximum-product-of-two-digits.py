class Solution:
    def maxProduct(self, n: int) -> int:
        ans=[]
        while n>0:
            ans.append(n%10)
            n=n//10
        ans.sort(reverse=True)
        return ans[0]*ans[1]