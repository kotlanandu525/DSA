class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        ans=0
        for num in range(num1,num2+1):
            ls=str(num)
            if len(ls)<3:
                continue
            else:
                for i in range(len(ls)-2):
                    f=ord(ls[i])
                    s=ord(ls[i+1])
                    t=ord(ls[i+2])
                    if (s>f and s>t) or (s<f and s<t):
                        ans+=1
        return ans           
