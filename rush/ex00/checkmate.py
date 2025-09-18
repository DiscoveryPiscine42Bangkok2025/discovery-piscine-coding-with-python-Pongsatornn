from typing import List, Tuple, Optional

PIECES = {"Q", "R", "B", "P"}

def _is_square(grid: List[str]) -> bool:
    n = len(grid)
    if n == 0:
        return False
    return all(len(row) == n for row in grid)

def _find_king(grid: List[str]) -> Optional[Tuple[int, int]]:
    found = [(i, j) for i, row in enumerate(grid)
             for j, ch in enumerate(row)
             if ch == "K"]
    if len(found) != 1:
        return None
    return found[0]

def _is_piece(ch: str) -> bool:
    return ch not in {".", "K"}

def _attacks_from_pawn(i: int, j: int, king: Tuple[int, int], is_white: bool = True) -> bool:

    king_i, king_j = king
    if is_white:
        return (king_i == i - 1) and (king_j == j - 1 or king_j == j + 1)
    else:
        return (king_i == i + 1) and (king_j == j - 1 or king_j == j + 1)

def _ray_hits_king(grid: List[str], i: int, j: int, di: int, dj: int, king: Tuple[int, int]) -> bool:
    n = len(grid)
    r, c = i + di, j + dj
    while 0 <= r < n and 0 <= c < n:
        ch = grid[r][c]
        if ch == "K":
            return True
        if _is_piece(ch):
            return False
        r += di
        c += dj
    return False

def is_king_in_check(board: str, white_pieces: bool = True) -> bool:
 
    try:
        grid = board.strip().splitlines()
        
        if not _is_square(grid):
            return False
            
        king = _find_king(grid)
        if king is None:
            return False

        n = len(grid)

        for i in range(n):
            row = grid[i]
            for j in range(n):
                ch = row[j]
                
                if ch == "P":
                    if _attacks_from_pawn(i, j, king, white_pieces):
                        return True
                        
                elif ch == "B": 
                    if (_ray_hits_king(grid, i, j, -1, -1, king) or
                        _ray_hits_king(grid, i, j, -1, +1, king) or
                        _ray_hits_king(grid, i, j, +1, -1, king) or
                        _ray_hits_king(grid, i, j, +1, +1, king)):
                        return True
                        
                elif ch == "R": 
                    if (_ray_hits_king(grid, i, j, -1, 0, king) or
                        _ray_hits_king(grid, i, j, +1, 0, king) or
                        _ray_hits_king(grid, i, j, 0, -1, king) or
                        _ray_hits_king(grid, i, j, 0, +1, king)):
                        return True
                        
                elif ch == "Q":  
                    if (_ray_hits_king(grid, i, j, -1, 0, king) or
                        _ray_hits_king(grid, i, j, +1, 0, king) or
                        _ray_hits_king(grid, i, j, 0, -1, king) or
                        _ray_hits_king(grid, i, j, 0, +1, king) or
                        _ray_hits_king(grid, i, j, -1, -1, king) or
                        _ray_hits_king(grid, i, j, -1, +1, king) or
                        _ray_hits_king(grid, i, j, +1, -1, king) or
                        _ray_hits_king(grid, i, j, +1, +1, king)):
                        return True

        return False
        
    except Exception:
        return False

def checkmate(board: str) -> None:
    if is_king_in_check(board):
        print("Success")
    else:
        print("Fail")

