class Solution:
    def check(self, nums: List[int]) -> bool:
        # ans=False
        # a=sorted(nums)
        # for i in range(len(nums)):
        #     b=[]
        #     for j in range(len(nums)):
        #         b.append(nums[(i+j)%len(nums)])
        #     if a==b:
        #         ans=True
        # return ans
        drop=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                drop+=1
        return drop<=1


        