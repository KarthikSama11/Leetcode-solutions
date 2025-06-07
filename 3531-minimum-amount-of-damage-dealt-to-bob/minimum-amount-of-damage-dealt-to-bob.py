import math
from functools import cmp_to_key

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        
        N = len(health)
        res = 0
        totaldamage = sum(damage)
        enemies = [(damage[i], math.ceil(health[i]/power)) for i in range(N)]
        enemies.sort(key = lambda x: (-x[0]/x[1]) )
        print(enemies)
        for dam, sec in enemies:
            res += totaldamage * sec
            totaldamage -= dam
        return res

