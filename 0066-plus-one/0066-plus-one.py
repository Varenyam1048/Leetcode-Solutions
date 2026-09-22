class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        ans=[]

        num = int("".join(str(digit) for digit in digits))

        num=num+1

        ans = [int(digit) for digit in str(num)]

        return ans 

