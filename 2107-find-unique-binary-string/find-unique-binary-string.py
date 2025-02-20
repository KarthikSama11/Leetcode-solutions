class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = 16
        # convert binary string to decimal
        def convert(s):
            base = 2
            power = 0
            res = 0
            for i in range(len(s)- 1, -1, -1):
                ch = s[i]
                digit = int(ch)
                res = res + (base ** power)* digit
                power += 1
            return res
        sets = set()
        for x in nums:
            num = convert(x)
            # print(num)
            sets.add(num)
        print(sets)
        print("------")

        for i in range(N + 1):
            if i in sets:
                continue
            ans = i
            
            binary = str(bin(ans))
            print(ans, binary)
            binary = binary[2::]
            return  "0" * (len(nums) - len(binary))  + binary
            

        return ""
