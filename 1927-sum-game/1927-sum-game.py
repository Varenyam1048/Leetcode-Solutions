class Solution:
    def sumGame(self, num: str) -> bool:

        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        diff = left_sum - right_sum
        qdiff = left_q - right_q

        
        if qdiff % 2 != 0:
            return True

       
        return diff + (qdiff // 2) * 9 != 0