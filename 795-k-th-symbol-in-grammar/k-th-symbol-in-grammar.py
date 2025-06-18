class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k):
            if n == 0 or k == 0:
                return False
            
            total = 2 ** n 
            mid = total//2
            print(n, mid, total)
            if k < mid:
                return dfs(n - 1, k)
            else:
                return not dfs(n-1, k - mid)
        res =  dfs(n-1,k-1)
        return 1 if res else 0
        final = [0]
        for _ in range(1, n):
            size = len(final)
            for i in range(size):
                val = 0
                if final[i] == 0:
                    val = 1
                final.append(val)
        return final[k - 1]
        """
        0 
        0 1
        0 1 1 0
        0 1 1 0 1 0 0 1
        n = 4 and k = 6
        """


