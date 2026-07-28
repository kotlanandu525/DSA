class Solution:
    def smallestPalindrome(self, s: str) -> str:
        m=len(s)//2
        half="".join(sorted(s[:m]))
        if len(s)%2==1:
            mid=s[m]
            return half+mid+half[::-1]
            
            
        return half+half[::-1]
                