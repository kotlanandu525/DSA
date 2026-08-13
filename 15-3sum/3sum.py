class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        ans=[]
        for i in range(n-2):
            f=nums[i]
            if nums[i]>0:
                break
            if  i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1
            while j<k:
                s=nums[j]+nums[k]
                if s==(-f):
                    ans.append([f,nums[j],nums[k]])
                    j+=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    
                    k-=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif s>-(f):
                    k-=1
                else:
                    j+=1
                
        return ans

