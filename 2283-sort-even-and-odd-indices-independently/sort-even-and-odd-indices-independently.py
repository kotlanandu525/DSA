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
        e=0
        o=0
        for i in range(len(nums)):
            if i%2==0:
                ans.append(even[e])
                e+=1
            else:
                ans.append(odd[o])
                o+=1
            
        return ans