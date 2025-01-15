class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows <= 1 or numRows > len(s):
            return s

        rs = {}  # content of rows
        r = 0  # current row
        d = 1  # direction 1 is forward, -1 is backward


        for i in range(len(s)):
            c = s[i]  # current character

            # insert character
            try:
                rs[r] += c
            except KeyError:
                rs[r] = c

            r += d  # update row

            # check if need to update direction
            if r <= 0:
                d = 1  # forward
            elif r >= (numRows-1):
                d = -1  # backward

        out = "".join([rs[i] for i in range(numRows)])
        return out
