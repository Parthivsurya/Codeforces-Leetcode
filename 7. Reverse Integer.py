class Solution:
    def reverse(self, x: int) -> int: 
        sign = -1 if x < 0 else 1
        x = abs(x)
        num = sign * abs(int(str(x)[::-1]))
        if num < -2**31 or num > 2**31 - 1:
            return 0
        return num