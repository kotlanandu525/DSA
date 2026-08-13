class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm=Counter(magazine)
        for ch in ransomNote:
            if ch in hm:
                hm[ch]-=1
                if hm[ch]==0:
                    del hm[ch]
            else:
                return False
        return True