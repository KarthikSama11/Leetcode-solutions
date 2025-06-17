class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = set()
        remains = defaultdict(int)
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls.add(i)
            else:
                remains[secret[i]] += 1
        for i in range(len(guess)):
            if i in bulls:
                continue
            if remains[guess[i]] > 0:
                cows += 1
                remains[guess[i]] -= 1
        res = str(len(bulls)) + "A" + str(cows) + "B"
        return res
            