class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        s=list(str(n))
        num=''
        for c in s:
            if c!='0':
                num+=c
        noo=int(num)
        num=list(num)
        s=0
        for n in num:
            s+=int(n)
        return noo*s
        
        



