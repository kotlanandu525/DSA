class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even=[]
        odd=[]
        ans=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        even.sort()
        odd.sort(reverse=True)
        for i in range(min(len(even),len(odd))):
            ans.append(even[i])
            ans.append(odd[i])
        if len(ans)!=len(nums):
            ans.append(even[-1])
        return ans