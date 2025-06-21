class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        candies = [1] * N
        res = N
        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                res += 1 + candies[i -1] - candies[i]
                candies[i] = candies[i - 1] + 1
        print(candies)
        for i in range(N - 2, -1, -1):
            if ratings[i + 1] < ratings[i] and candies[i] <= candies[i + 1]:
                res += candies[i + 1] - candies[i] +1
                candies[i] = candies[i + 1] + 1
        print(candies)
        return res
