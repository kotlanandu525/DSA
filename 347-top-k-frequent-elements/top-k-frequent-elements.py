class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=Counter(nums)
        heap=[]
        for e,f in f.items():
            heapq.heappush(heap,(f,e))
            while len(heap)>k:
                heapq.heappop(heap)
        return [e for f,e in heap]
        