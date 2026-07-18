class CheckMate:
    def __init__(self, map):
        self.map = map
    def check(self) -> int:
        return 0
    def checkmate(self) -> int:
        return 0

class Piece:
    def __init__(self, pos: str, map: list, checkmate: CheckMate):
        self.pos = pos
        self.map = map
        self.checkmate = checkmate
    def KingMove(self, pos: str, cout: int) -> int:
        return 0
    def QueenMove(self, pos: str) -> int:
        return 0
    def BishopMove(self, pos: str) -> int:
        return 0
    def RookMove(self, pos: str) -> int:
        decision = 0
        if self.pos[0] == self.pos[2] or self.pos[1] == self.pos[3]:
            decision = 1
        return decision
    def PawnMove(self, pos: str) -> int:
        return 0
    def KnightMove(self, pos: str) -> int:
        return 0
