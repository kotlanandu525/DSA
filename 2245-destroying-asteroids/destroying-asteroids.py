class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroid=sorted(asteroids)
        for m in asteroid:
            if m>mass:
                return False
            mass+=m
        return True
