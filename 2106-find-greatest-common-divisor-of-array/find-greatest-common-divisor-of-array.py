class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcdd(a,b):
            while b:
                a,b=b,a%b
            return a
        return gcdd(min(nums),max(nums))
        