class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s=0
        p=1
        temp=n

        while temp:
            digit=temp%10
            s+=digit
            p*=digit
            temp//=10

        x=s+p

        return n%x==0
