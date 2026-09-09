class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        start = 1000

        while start <= n:
            end = min(n, start * 10 - 1)
            count = end - start + 1
            length = len(str(start))
            commas = (length - 1) // 3
            ans += count * commas
            start *= 10

        return ans