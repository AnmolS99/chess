from move import Move
from player import Player
from pieces.piece import Piece

piece_int = 3

class Knight(Piece):

    def __init__(self):
        super().__init__()

    @staticmethod
    def get_moves(board, pos, possible_en_passant, castling_rights, opp_capture_moves, color_value):
        piece_value = piece_int * color_value
        moves = []
        x, y = pos
        if x > 1:
            if y > 0 and board[x - 2][y - 1] * color_value <= 0:
                moves.append(Move(pos, (x - 2, y - 1), piece_value))
            if y < 7 and board[x - 2][y + 1] * color_value <= 0:
                moves.append(Move(pos, (x - 2, y + 1), piece_value))
        if x > 0:
            if y > 1 and board[x - 1][y - 2] * color_value <= 0:
                moves.append(Move(pos, (x - 1, y - 2), piece_value))
            if y < 6 and board[x - 1][y + 2] * color_value <= 0:
                moves.append(Move(pos, (x - 1, y + 2), piece_value))
        if x < 6:
            if y > 0 and board[x + 2][y - 1] * color_value <= 0:
                moves.append(Move(pos, (x + 2, y - 1), piece_value))
            if y < 7 and board[x + 2][y + 1] * color_value <= 0:
                moves.append(Move(pos, (x + 2, y + 1), piece_value))
        if x < 7:
            if y > 1 and board[x + 1][y - 2] * color_value <= 0:
                moves.append(Move(pos, (x + 1, y - 2), piece_value))
            if y < 6 and board[x + 1][y + 2] * color_value <= 0:
                moves.append(Move(pos, (x + 1, y + 2), piece_value))
        return moves
    
    @staticmethod
    def get_capture_moves(board, pos, possible_en_passant, color_value):
        return Knight.get_moves(board, pos, possible_en_passant, None, None, color_value)