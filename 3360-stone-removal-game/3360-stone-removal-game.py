class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones=n
        remove=10

        while stones>=remove:
            stones-=remove
            remove-=1

        return remove%2==1

        