class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a=bin(x)[2:]
        b=bin(y)[2:]
        a=a.zfill(32)
        b=b.zfill(32)
        ans=0
        for i in range(32):
            if a[i]!=b[i]:
                
                ans+=1
        return ans

            
