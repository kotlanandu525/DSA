class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq=Counter(text)
        b=freq['b']
        a=freq['a']
        l=freq['l']//2
        o=freq['o']//2
        n=freq['n']
        return min(b,a,l,o,n)