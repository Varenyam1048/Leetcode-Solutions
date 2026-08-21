class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a 
            
        def lcm(a, b):
            return a * b // gcd(a, b)

        def count(x):
            total = 0
            n = len(coins)

            for mask in range(1, 1 << n):

                curr_lcm = 1
                bits = 0
                valid = True

                for i in range(n):
                    if mask & (1 << i):

                        bits += 1

                        curr_lcm = lcm(curr_lcm, coins[i])

                        if curr_lcm > x:
                            valid = False
                            break

                if valid:
                    amount = x // curr_lcm

                    if bits % 2 == 1:
                        total += amount
                    else:
                        total -= amount

            return total

        low = 1
        high = max(coins) * k

        while low < high:

            mid = (low + high) // 2

            if count(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low