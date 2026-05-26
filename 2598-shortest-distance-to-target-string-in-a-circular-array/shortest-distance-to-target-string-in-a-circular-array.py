class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        c=0
        n=len(words)
        for i in range(len(words)):
            
            if words[(startIndex+i)%n]==target or words[(startIndex-i)%n]==target:
                
                return c
            c+=1
        return -1


        