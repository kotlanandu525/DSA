class Solution:
    def isGood(self, nums: List[int]) -> bool:
        seen=set()
        n=len(nums)-1
        dup=False
        for num in nums:
            if num>n:return False
            if num in seen:
                
                if num<n or dup:
                    return False
                dup=True
                
            seen.add(num)
        return True