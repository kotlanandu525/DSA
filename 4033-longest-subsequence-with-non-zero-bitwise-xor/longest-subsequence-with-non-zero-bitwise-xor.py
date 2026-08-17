class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        x=0
        has=False
        for num in nums:
            x^=num
            if num!=0:
                has=True
        if x!=0:
            return len(nums)
        else:
            if has:
                return len(nums)-1
        return 0


