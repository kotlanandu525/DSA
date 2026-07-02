class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        hm=defaultdict(lambda:[0]*len(votes[0]))
        for word in votes:
            for i,ch in enumerate(word):
                hm[ch][i]+=1
        s=sorted(hm.keys())
        s=sorted(s,key=lambda x:hm[x],reverse=True)
        return "".join(s)