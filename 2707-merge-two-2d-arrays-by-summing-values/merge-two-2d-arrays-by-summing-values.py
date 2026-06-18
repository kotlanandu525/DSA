class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        d={}
        nums1.sort()
        nums2.sort()
        for i,v in nums1+nums2:
            d[i]=d.get(i,0)+v
        ans=[[x,d[x]] for x in d.keys()]
        return sorted(ans)