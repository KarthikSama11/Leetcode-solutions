class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def dfs(n, k):
            if n == 0 or k == 0:
                return False
            
            total = 2 **(n )
            mid = total//2
            print(n, mid, total)
            if k < mid:
                return dfs(n - 1, k)
            else:
                return not dfs(n-1, k - mid)
        res =  dfs(n-1,k-1)
        return 1 if res else 0
        """
        0 
        0 1
        0 1 1 0
        0 1 1 0 1 0 0 1
        n = 4 and k = 6
        """


