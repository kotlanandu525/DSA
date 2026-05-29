class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans=0
        p=0
        q=0
        while p<len(nums1) and q<len(nums2):
            if nums1[p]<=nums2[q]:
                    
                ans=max(ans,q-p)
                q+=1
            else:
                p+=1
        return ans
        


