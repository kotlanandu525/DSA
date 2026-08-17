class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap=[]
        for mat in matrix:
            for n in mat:
                heappush(heap,-n)
                if len(heap)>k:
                    heappop(heap)
        return -heap[0]