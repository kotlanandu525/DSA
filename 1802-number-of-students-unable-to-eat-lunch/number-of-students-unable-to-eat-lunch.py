class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt=[students.count(0),students.count(1)]
        for s in sandwiches:
            if cnt[s]==0:
                break
            cnt[s]-=1
        return sum(cnt)


        