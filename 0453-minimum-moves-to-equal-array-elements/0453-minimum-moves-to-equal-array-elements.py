class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_value=min(nums)
        ans=0

        for num in nums:
            ans+=num-min_value

        return ans 