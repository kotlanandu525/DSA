class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c=0
        s=[]
        t=[]
        for x,y in zip(s1,s2):
            if x!=y:
                c+=1
                s.append(x)
                t.append(y)
        if c==0 or c==2 and sorted(s)==sorted(t):
            return True
        else:
            return False