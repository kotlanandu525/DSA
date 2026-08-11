class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k!=0:
            return False
        nums.sort()
        for _ in range(len(nums)//k):
            f=nums[0]
            for i in range(k):
                if f in nums:
                    nums.remove(f)
                    f+=1
                else:
                    return False
        return True