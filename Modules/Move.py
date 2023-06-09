class Move():
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4,
                   "5": 3, "6": 2, "7": 1, "8": 0}
    rowToRanks = {v:k for k, v in ranksToRows.items()}
    filesToCols = {"a": 0, "b": 1, "c": 2, "d": 3,
                   "e": 4, "f": 5, "g": 6, "h":7}
    colsToFiles = {v:k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.enPassant = False
        self.ksCastling = False
        self.qsCastling = False
        self.pawnPromotion = False
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveId = self.startRow*1000 + self.startCol*100 + self.endRow*10 + self.endCol
        self.Position = board

    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveId == other.moveId
        return False
            
    def getChessNotation(self):
        if self.enPassant:
            return self.colsToFiles[self.startCol]+'X'+self.getRankFile(self.endRow, self.endCol)
        elif self.ksCastling:
            return "O-O"
        elif self.qsCastling:
            return "O-O-O"

        if self.pieceCaptured == "__":
            if self.pieceMoved[1] == "p":
                return self.getRankFile(self.endRow, self.endCol)
            else:
                return self.pieceMoved[1]+self.getRankFile(self.endRow, self.endCol)
        else:
            if self.pieceMoved[1] == "p":
                return self.colsToFiles[self.startCol]+'X'+self.getRankFile(self.endRow, self.endCol)
            else:
                return self.pieceMoved[1]+'X'+self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self,r ,c):
        return self.colsToFiles[c] + self.rowToRanks[r]
