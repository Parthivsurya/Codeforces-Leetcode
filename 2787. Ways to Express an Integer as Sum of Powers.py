class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        def power_sum(remaining, num):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if num ** x > remaining:
                return 0
            take = power_sum(remaining - num**x, num + 1)
            skip = power_sum(remaining, num + 1)
            return take + skip
        return power_sum(n, 1)