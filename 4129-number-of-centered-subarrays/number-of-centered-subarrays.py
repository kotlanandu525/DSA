class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        for i in range(n):
            s=0
            seen=set()
            for j in range(i,n):
                s+=nums[j]
                seen.add(nums[j])
                if s in seen:
                    cnt+=1
        return cnt