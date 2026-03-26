class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        rsum=[]
        csum=[]
        s=0
        for arr in grid:
            s+=sum(arr)
            rsum.append(s)       
        for i in range(len(grid[0])):
            c=0
            for j in range(len(grid)):
                c+=grid[j][i]
            csum.append(c)
        tot=rsum[-1]
        for i in range(len(rsum)):
            if rsum[i]==(tot-rsum[i])  :
                return True
        tot=sum(csum)
        prefix=0
        for i in range(len(csum)):
            prefix+=csum[i]
            if prefix==(tot-prefix)  :
                return True
        
        return False