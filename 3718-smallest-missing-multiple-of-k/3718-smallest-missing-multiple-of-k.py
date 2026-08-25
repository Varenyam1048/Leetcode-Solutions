class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s = set(nums)

        x = k

        while x in s:
            x += k

        return x