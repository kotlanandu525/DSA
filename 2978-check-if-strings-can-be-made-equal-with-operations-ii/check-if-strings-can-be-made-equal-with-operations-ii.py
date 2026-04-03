class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        k=len(s1)
        a,b,c,d=[],[],[],[]
        
        for i in range(k):
            if i%2==0:
                a.append(s1[i])
                b.append(s2[i])
            else:
                c.append(s1[i])
                d.append(s2[i])
        return sorted(a)==sorted(b) and sorted(c)==sorted(d)   
        