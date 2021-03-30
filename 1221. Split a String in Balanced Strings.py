class Solution:
    def balancedStringSplit(self, s: str) -> int:
        m = c = 0
        for st in s:
            if st == 'L': c += 1
            if st == 'R': c -= 1
            if c == 0: m += 1
        return m
        