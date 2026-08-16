class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        i=len(word1)-1
        j=len(word2)-1
        memo={}
        def solve(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i]==word2[j]:
                memo[(i,j)]=solve(i-1,j-1)
            
            else:
                 memo[(i,j)]=1+min(
                    solve(i-1,j),
                    solve(i,j-1),
                    solve(i-1,j-1)
                )
            return memo[(i,j)]
        
        return solve(i,j)
            