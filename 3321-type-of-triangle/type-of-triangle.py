class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c = nums
        if a+b <= c or a + c  <= b or b + c <= a:
            return "none"
        if len(set(nums)) == 2:
            return "isosceles"
        if a == b and b == c:
            return "equilateral"
        if a != b and b != c:
            return "scalene"
        
        