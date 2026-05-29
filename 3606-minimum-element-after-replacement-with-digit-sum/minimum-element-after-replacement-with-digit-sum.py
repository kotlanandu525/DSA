class Solution:
    def minElement(self, nums: List[int]) -> int:
        temp=[]
        for num in nums:
            s=0
            while num>0:
                s+=num%10
                num//=10
            temp.append(s)
        return min(temp)
        