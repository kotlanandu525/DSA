class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n=len(candyType)
        eat=set(candyType)
        if n//2<len(eat):
            return n//2
        else:
            return len(eat)
