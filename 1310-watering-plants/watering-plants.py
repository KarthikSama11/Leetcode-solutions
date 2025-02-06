class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        bucket = capacity
        steps = 0
        """
         plants.insert(0,0)
        [2,2,3,3] 5, 0
        [0,2,3,3] 3, 1
        [0,0,3,3] 1, 2
        [0,0,0,3] 2, 2+ 4 + 1
        """
        for i, plant in enumerate(plants):
            if bucket < plant:
                steps += 2 * i
                bucket = capacity
            steps += 1
            bucket -= plant
        return steps

            


