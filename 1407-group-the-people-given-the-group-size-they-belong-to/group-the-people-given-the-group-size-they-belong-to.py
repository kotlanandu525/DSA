class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        hm=defaultdict(list)
        for i,val in enumerate(groupSizes):
            hm[val].append(i)
        ans=[]
        sorted(hm.items() )
        for k,v in hm.items():
            for i in range(0,len(v),k):
                ans.append(v[i:i+k])
        return ans
