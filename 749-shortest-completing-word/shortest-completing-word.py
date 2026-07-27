class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        ans=''
        for ch in licensePlate:
            if ch.isalpha():
                ans+=ch.lower()
        d=Counter(ans)
        res=None
        for word in words:
            f=Counter(word)
            valid=True
            for ch in d:
                if f[ch]<d[ch]:
                    valid=False
                    break
            if valid:
                if res is None or len(word)<len(res):
                    res=word
        return res
            
