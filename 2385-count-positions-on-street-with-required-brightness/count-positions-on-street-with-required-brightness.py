class Solution:
    def meetRequirement(self, n: int, lights: List[List[int]], requirement: List[int]) -> int:
        mini = 1e9
        street = defaultdict(int)
        weirdos = set()
        for i,j in lights:
            left =  i - j
            right = i + j
            if left == right:
                weirdos.add(left)
            street[max(0,left)] += 1
            street[min(n,right + 1)] -= 1
            # mini = min(left, mini)
        count = 0
        ans = 0
        for i in range( n):
            count += street[i]
            if 0 <= i < n :
                print(i, count)
                # comp += count
                # x = 1 if i in weirdos else 0
                if requirement[i] <= count :
                    ans += 1
                
        # print(sorted(street.items()))
        # print(weirdos)
        
        return ans 

        
            