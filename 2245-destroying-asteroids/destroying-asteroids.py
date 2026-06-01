class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroid=sorted(asteroids)
        for i in range(len(asteroids)):
            if mass>=asteroid[i]:
                mass+=asteroid[i]
            else:
                return False
        return True
