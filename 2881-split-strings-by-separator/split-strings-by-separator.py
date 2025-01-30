class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        ans =[]
        build = ""
        for word in words:
            if len(build):
                        ans.append(build)
                        build = ""
            for i, c in enumerate(word):
                if c == separator:
                    if len(build):
                        ans.append(build)
                        build = ""
                    continue
                build = build + c
        if len(build):
                        ans.append(build)
                        build = ""
        return ans
