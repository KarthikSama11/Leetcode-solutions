class Solution:
    def dividePlayers(self, skills: List[int]) -> int:
        chemistry = 0
        N = len(skills)
        totalskill = sum(skills)
        noofteams = N // 2
        if N % 2 != 0 or totalskill % noofteams != 0 :
            return -1
        reqskill = totalskill // noofteams
        skills.sort()
        l = 0
        r = N - 1
        while l < r:
            chemistry += skills[l] * skills[r]
            if skills[l] + skills[r] != reqskill:
                return -1
            l += 1
            r -= 1
        return chemistry

