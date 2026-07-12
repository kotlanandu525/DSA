class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        cd=0
        for ch in s:
            if ch=='(':  
                cd+=1
                ans=max(ans,cd)
                    
            elif  ch==')':
                cd-=1
        return ans
