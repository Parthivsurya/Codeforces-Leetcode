class Solution:
    def isPalindrome(self, x: int) -> bool:
        new=str(x)
        return new[::-1]==new
        
        