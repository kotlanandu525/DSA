class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        l,u=n-1,0
        st=[]
        for i in range(n):
            while st and nums[st[-1]]>nums[i]:
                l=min(l,st.pop())
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]<nums[i]:
                u=max(u,st.pop())
            st.append(i)
        return 0 if l>=u else u-l+1
