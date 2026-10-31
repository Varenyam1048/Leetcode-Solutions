class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row=[1]

        for x in range(rowIndex):
            next_row=[1]

            for i in range(len(row)-1):
                next_row.append(row[i]+row[i+1])

            next_row.append(1)

            row=next_row

        return row 

        


