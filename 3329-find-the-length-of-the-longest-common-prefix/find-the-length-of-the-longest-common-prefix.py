class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        pref=set()

        for n in arr1:
            s=''
            for ch in str(n):
                s+=ch
                if s not in pref:
                    pref.add(s)
        ans=0
        for n in arr2:
            s=''
            for ch in str(n):
                s+=ch
                if s in pref and len(s)>ans:
                    ans=len(s)
        return ans
        
             