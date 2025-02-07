class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        if rows==1 or cols==1:
            return True

        toeplitz = []
        # checks up left side below top row
        for r0 in range(rows-2, 0, -1):
            val = matrix[r0][0]
            _toeplitz = False
            for i in range(r0+1,rows):
                r = i
                c = i-r0
                try:
                    if matrix[r][c] == val:
                        _toeplitz = True
                    else:
                        _toeplitz = False
                        break
                except IndexError:
                    _toepllitz = False
                    break
            toeplitz.append(_toeplitz)
            if _toeplitz == False:
                break

        # checks starting at top row
        for i in range(cols-1):
            val = matrix[0][i]
            _toeplitz = False
            for r in range(1,rows):
                try:
                    if matrix[r][r+i] == val:
                        _toeplitz = True
                    else:
                        _toeplitz = False
                        break
                except IndexError:
                    break
            toeplitz.append(_toeplitz)
            if _toeplitz == False:
                break

        return True in toeplitz and not False in toeplitz
