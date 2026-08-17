class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        heap=[]
        for i in range(n):   
            heappush(heap,(matrix[i][0],i,0))
        
        val=0
        for _ in range(k):
            val,i,j=heappop(heap)
            if j+1<n:
                heappush(heap,(matrix[i][j+1],i,j+1))
        return val