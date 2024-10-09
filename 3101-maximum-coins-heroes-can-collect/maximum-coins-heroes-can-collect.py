class Solution:
    def maximumCoins(self, heroes: List[int], monsters: List[int], coins: List[int]) -> List[int]:
        monstercoins = []
        ans = []
        N = len(monsters)
        for i in range(len(monsters)):
            monstercoins.append([monsters[i], coins[i]])
        monstercoins.sort()
        pre = 0
        for i in range(N):
            pre += monstercoins[i][1]
            monstercoins[i][1] = pre
        for hero in heroes:
            paisal = 0
            l, r = 0, N - 1
            # print(hero)
            while l <= r:
                mid = (l + r)//2
                # print(l, r)
                if monstercoins[mid][0] <= hero:
                    paisal = monstercoins[mid][1]
                    l = mid + 1
                else:
                    r = mid - 1
            ans.append(paisal)
            # print("----------------")
        return ans