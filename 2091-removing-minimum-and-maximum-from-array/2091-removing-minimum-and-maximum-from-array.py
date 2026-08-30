class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        max_val = nums[0]
        min_val = nums[0]

        max_index = 0
        min_index = 0

        for i, value in enumerate(nums):
            if value > max_val:
                max_val = value
                max_index = i

            if value < min_val:
                min_val = value
                min_index = i

        case1 = max(max_index, min_index) + 1
        case2 = n - min(max_index, min_index)
        case3 = min(max_index, min_index) + 1 + n - max(max_index, min_index)

        return min(case1, case2, case3)