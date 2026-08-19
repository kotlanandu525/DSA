class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n=len(groups)
        prev=groups[0]
        ans=[words[0]]
        for g in range(1,n):
            if prev!=groups[g]:
                ans.append(words[g])
                prev=groups[g]
        return ans
