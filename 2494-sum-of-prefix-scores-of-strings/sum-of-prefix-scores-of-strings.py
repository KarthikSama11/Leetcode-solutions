class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        #rabin karp to store hashes
        # base = 29
        # mod = 10**7
        # power = 0
        # prefixes = {}
        # ans = 0
        # words.sort()
        hashset = defaultdict(int)
        for word in words:
            for i in range(len(word)):
                hashset[word[:i+1]] += 1
        ans = []
        for word in words:
            count = 0
            for i in range(len(word)):
                if word[:i + 1] in hashset:
                    count += hashset[word[:i+1]]
            ans.append(count)
        # print(hashset)
        return ans