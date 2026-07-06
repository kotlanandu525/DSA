class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        
        max_end=0

        c=0
        for st,end in intervals:
            if end>max_end:
                c+=1
            
                max_end=end
        return c
            
