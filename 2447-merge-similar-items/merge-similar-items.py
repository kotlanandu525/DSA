class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        m=len(items1)
        n=len(items2)
        ans=[]
        i=0
        j=0
        while i<m and j<n:
            
            arr1=items1[i]
            arr2=items2[j]
            if arr1[0]==arr2[0]:
                ans.append([arr1[0],arr1[1]+arr2[1]])
                i+=1
                j+=1
            elif arr1[0]>arr2[0]:
                ans.append(arr2)
                j+=1
            else:
                ans.append(arr1)
                i+=1
        if i<m:
            ans.extend(items1[i:])
        else:
            ans.extend(items2[j:])
        return ans