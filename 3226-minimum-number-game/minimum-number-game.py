class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        ans=[]
        heap=[]
        for x in nums:
            heapq.heappush(heap,x)
        while heap:
            a=heapq.heappop(heap)
            b=heapq.heappop(heap)
            ans.append(b)
            ans.append(a)
        return ans