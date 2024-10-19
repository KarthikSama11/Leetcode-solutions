class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        self.arr = []
        def dfs(n):
            if n == 1:
                self.arr.append("0")
                return
            
            dfs(n - 1)
            # brr = reversed(self.arr)
            brr = []
            for i in reversed(self.arr):
                if i == "1":
                    brr.append("0")
                else:
                    brr.append("1")
            self.arr.append("1")
            self.arr = self.arr + brr
            return
        dfs(n)
        if k > len(self.arr):
            return "0"
        # print("".join(self.arr))
        return self.arr[k - 1]