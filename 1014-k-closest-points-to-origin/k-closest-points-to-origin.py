class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        ans=[]
        for point in points:
            a,b=point
            d=(a*a+b*b)**0.5
            heapq.heappush(heap,(d,point))
        while k>0:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans