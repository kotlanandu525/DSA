class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        nums.sort()
        c=0
        i=0
        j=n-1
        while i<=j:
            s=nums[i]+nums[j]
            if i==j:
                if nums[i]<=limit:
                    c+=1
                    i+=1
                    j-=1
            elif s<=limit:
                c+=1
                j-=1
                i+=1
            else:
                c+=1
                j-=1
            
        
        return c
