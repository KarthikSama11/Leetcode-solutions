class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        logs = set((u, t) for u, t in logs)
        dic = defaultdict(int)
        for u, t in logs:
            dic[u] += 1
        uam = [0] * k
        for _, total in dic.items():
            if total == 0:
                continue
            uam[total - 1] += 1
        return uam