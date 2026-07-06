class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        r=5*len(arr)//100
        mat=arr[r:len(arr)-r]
        return sum(mat)/len(mat)