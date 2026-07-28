class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        freq=Counter(nums)
        ans=[]
        l=n//3
        for k,v in freq.items():
            if v>l:
                ans.append(k)
        return ans