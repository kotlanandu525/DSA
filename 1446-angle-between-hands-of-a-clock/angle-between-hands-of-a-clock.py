class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m=minutes*6
        h=(hour%12)*30+(minutes)*0.5
        angle=abs(m-h)
        return min(angle,360-angle)