class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        max_l=0
        max_s=s[0]
        def fun(l,r):
            while (l>=0 and r<n) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        for i in range(n):
            odd=fun(i,i)
            even=fun(i,i+1)
            if len(odd)>len(max_s):
                max_s=odd
            if len(even)>len(max_s):
                max_s=even
        return max_s