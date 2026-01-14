class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        if p=="*":
            return True
        else:
            for i in range(len(p)):
                if p[i] == '?':
                    continue
                if p[i] != s[i]:
                    return False
Solution1 = Solution()
print(Solution1.isMatch("cb","?b"))