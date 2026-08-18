class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        closesum=float('inf')
        for i in range(n-2):
            l=i+1
            r=n-1
            
           
            while l<r:
                summ=nums[i]+nums[l]+nums[r]
                
                if abs(summ-target)<abs(closesum-target):
                    closesum=summ
                if summ==target:
                    return target
                elif summ>target:
                    r-=1
                else:
                    l+=1
        return closesum