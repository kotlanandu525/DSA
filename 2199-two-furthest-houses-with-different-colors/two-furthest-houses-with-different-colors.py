class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        ans=0
        for i in range(len(colors)):
            c=colors[i]
            for j in range(i+1,len(colors)):
                if c!=colors[j]:
                    ans=max(ans,abs(i-j))
        return ans
