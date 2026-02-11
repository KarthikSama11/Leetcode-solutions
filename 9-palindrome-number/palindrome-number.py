class Solution:
    def isPalindrome(self, x: int) -> bool:
        #negative numbers are automatically false
        #convert the number to string 
        #then compare right and left of the strings
        # or you could copy the original number just build the new number 
        if x < 0:
            return False
        copy_x = x
        y = 0

        while copy_x:
            y = y * 10 + copy_x%10
            copy_x = copy_x//10
        return x == y
