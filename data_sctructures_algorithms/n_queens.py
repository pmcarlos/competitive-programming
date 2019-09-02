class QueensProblem:
    def __init__(self, numOfQueens):
        self.numOfQueens = numOfQueens
        self.chessTable = [
            [None for i in range(numOfQueens)] for j in range(numOfQueens)
        ]

    def solveQueensProblem(self):

        if self.solve(0):
            self.printQueens()
        else:
            print("There is no solution...")

    def solve(self, colIndex):

        if colIndex == self.numOfQueens:
            return True

        for rowIndex in range(self.numOfQueens):

            if self.isPlaceValid(rowIndex, colIndex):

                self.chessTable[rowIndex][colIndex] = 1

                if self.solve(colIndex + 1):
                    return True

                # BACKTRACK
                self.chessTable[rowIndex][colIndex] = 0

        return False

    def isPlaceValid(self, row, col):
        # Check this row on left side
        for i in range(col):
            if self.chessTable[row][i] == 1:
                return False
        # Check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.chessTable[i][j] == 1:
                return False

        # Check lower diagonal on left side
        for i, j in zip(range(row, self.numOfQueens, 1), range(col, -1, -1)):
            if self.chessTable[i][j] == 1:
                return False

        return True

    def printQueens(self):

        for i in range(self.numOfQueens):
            for j in range(self.numOfQueens):

                if self.chessTable[i][j] == 1:
                    print(" * ", end=""),
                else:
                    print(" - ", end=""),

            print("\n")


if __name__ == "__main__":

    queensProblem = QueensProblem(5)
    queensProblem.solveQueensProblem()

