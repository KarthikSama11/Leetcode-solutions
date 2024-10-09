class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        line = [0]*(101)
        ansyear = -1
        ansppl = 0
        for s,e in logs:
            line[s - 1950] += 1
            line[e - 1950] -= 1
        print(line)
        ppl = 0
        for year, v in enumerate(line):
            ppl += v
            if line[year] == 0:
                continue
            if ppl > ansppl:
                ansyear = 1950 + year
                ansppl = ppl
            # print(ppl, ansppl, year + 1950)
        return ansyear