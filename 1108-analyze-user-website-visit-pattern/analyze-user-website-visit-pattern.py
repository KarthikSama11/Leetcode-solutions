class Solution:
    def mostVisitedPattern(self, username: List[str], timestamps: List[int], websites: List[str]) -> List[str]:
        final_map = defaultdict(int)
        res = 0
        res_list = []
        #build the user version of the sites visited
        user_map = defaultdict(list)
        #hash all words/websites to numbers 
        for user, site, stamp in sorted(zip(username, websites, timestamps), key = lambda x: (x[0], x[2])):
            user_map[user].append(site)
        def patterngenerator(nums, k):
            res = set()
            def recurse(i, k, combo):
                #base:
                if k == 0:
                    res.add(tuple(combo))
                    return 
                if i >= len(nums):
                    return
                #include
                combo.append(nums[i])
                recurse(i + 1, k - 1, combo)
                combo.pop()
                #exclude
                recurse(i + 1, k, combo)
            recurse(0, 3, [])
            return res
        user_patterns = defaultdict(set)
        for user, sitesvisited in user_map.items():
            user_patterns[user] = patterngenerator(sitesvisited, 3)
        print(user_patterns)
        for user, patterns in user_patterns.items():
            for pattern in patterns:
                final_map[pattern] += 1
                if final_map[pattern] > res:
                    res = final_map[pattern] 
                    res_list = list(pattern)
                if final_map[pattern] == res:
                        res_list = list(pattern) if list(pattern) < res_list else res_list
        return res_list

            