class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num=str(nums[i])
            total=0

            for digit in num:
                total+= int(digit)


            
            if total==i:
                return i
            
            
        return -1