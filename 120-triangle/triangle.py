class Solution:
    def minimumTotal(self, tri: List[List[int]]) -> int:
        
        n=len(tri)
        for i in range(n-2,-1,-1):
            for j in range(i+1):
                tri[i][j]+=min(tri[i+1][j],tri[i+1][j+1])
        return tri[0][0]
