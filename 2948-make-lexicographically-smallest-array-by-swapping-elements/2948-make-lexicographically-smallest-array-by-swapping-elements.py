class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        
        arr = sorted((value, i) for i, value in enumerate(nums))

        ans = [0] * len(nums)

        start = 0

        while start < len(arr):

            end = start

           
            while end + 1 < len(arr) and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

           
            indices = sorted(arr[i][1] for i in range(start, end + 1))

            
            values = [arr[i][0] for i in range(start, end + 1)]

           
            for i in range(len(indices)):
                ans[indices[i]] = values[i]

            start = end + 1

        return ans