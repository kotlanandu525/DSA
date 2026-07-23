class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
        ans=0
        for k in freq.keys():
            if freq[k]==1:
                ans+=k
        return ans