class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            for a in range(len(mat)):
                for b in range(a,len(mat)):
                    mat[a][b],mat[b][a]=mat[b][a],mat[a][b]
            for arr in mat:
                arr.reverse()
            if mat==target:
                return True
        return False
        

            