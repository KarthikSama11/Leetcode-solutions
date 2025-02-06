class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        l = 0
        N = len(plants)
        r = N - 1
        A = capacityA
        B = capacityB
        refills = 0
        while l < r:
            if A < plants[l]:
                A = capacityA
                refills += 1
            A -= plants[l]
            if B < plants[r]:
                B = capacityB
                refills += 1
            B -= plants[r]
            l += 1
            r -= 1
        if l == r:
            if (A >= B and A < plants[l]) or (A <= B and B < plants[r]):
                refills += 1
            
        return refills
                
            
