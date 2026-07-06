class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hm=Counter(nums)
        c=0
        

        for n in hm.keys():
            diff=(n-k)
            if k>0 and diff in hm:
                c+=1
            elif k==0 and hm[n]>1:
                c+=1
        return c
