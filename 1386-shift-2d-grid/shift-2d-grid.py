class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        k=k%(m*n)
        ans=[]
        for i in range(m):
            for j in range(n):
                ans.append(grid[i][j])
        ans=ans[-k:]+ans[:-k]
        k=0
        for i in range(m):
            for j in range(n):
                grid[i][j]=ans[k]
                k+=1
        return grid