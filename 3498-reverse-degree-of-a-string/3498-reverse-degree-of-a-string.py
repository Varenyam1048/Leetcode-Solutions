class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((26 - (ord(c) - 97)) * (i + 1) for i, c in enumerate(s))