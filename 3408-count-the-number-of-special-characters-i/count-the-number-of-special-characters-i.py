class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        s=set()
        c=0
        for l in word:
            s.add(ord(l))
        for l in s:
            if l-32 in s:
                c+=1
        return c
        