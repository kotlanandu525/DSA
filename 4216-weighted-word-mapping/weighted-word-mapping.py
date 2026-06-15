class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        
        ans=''
        for word in words:
            w=0
            for ch in word:
                w+=weights[ord(ch)-ord('a')]
            w=w%26
            ans+=chr(ord('z')-w)
        return ans