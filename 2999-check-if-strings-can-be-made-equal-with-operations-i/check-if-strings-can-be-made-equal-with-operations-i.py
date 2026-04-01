class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        # hm={}
        # # for a,b in zip(s1,s2):
        # for i in range(4):
        #     hm[i%2]=
        return sorted(s1[0]+s1[2])==sorted(s2[0]+s2[2]) and sorted(s1[1]+s1[3])==sorted(s2[1]+s2[3])

        