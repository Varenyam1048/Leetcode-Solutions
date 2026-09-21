class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        ans = [0] * k
        dp = [0] * k

        for num in nums:
            num %= k
            cur = [0] * k

            
            cur[num] = 1

            
            for r, count in enumerate(dp):
                cur[(r * num) % k] += count

            
            for r in range(k):
                ans[r] += cur[r]

            dp = cur

        return ans