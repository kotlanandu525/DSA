class Solution:
    def countAlternatingSubarrays(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        prev=nums[0]
        ans=0
        for e in nums:
            if prev!=e:
               l+=1
            else:
                l=1
             
            ans+=l
            prev=e
        return ans