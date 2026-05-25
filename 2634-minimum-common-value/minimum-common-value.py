class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        p=0
        q=0
        while p<len(nums1) and q<len(nums2):
            if nums1[p]==nums2[q]:
                return nums1[p]
            elif nums1[p]<nums2[q]:
                p+=1
            else:
                q+=1
        return -1