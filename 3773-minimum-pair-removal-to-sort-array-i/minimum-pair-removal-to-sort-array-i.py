class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        arr=nums[:]
        n=len(nums)
        op=0
        def issort(arr):
            for i in range(len(arr)-1):
                if arr[i]>arr[i+1]:
                    return False
            return True
        while  not issort(arr):
            min_sum=float("inf")
            for i in range(len(arr)-1):
                if arr[i]+arr[i+1]<min_sum:
                    min_sum=arr[i]+arr[i+1]
                    idx=i
                    
            arr[idx]=min_sum
            arr.pop(idx+1)
            op+=1
        return op