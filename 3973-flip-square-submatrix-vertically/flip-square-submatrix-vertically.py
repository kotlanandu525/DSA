class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        # for i in range(y,k+1):
        #     for j in range(x,k+1):
        p,q=0,0
        for i in range(y,y+k):
            p=x
            q=x+k-1
            while(p<q):
                grid[p][i],grid[q][i]=grid[q][i],grid[p][i]
                p+=1
                q-=1
        return grid
            
