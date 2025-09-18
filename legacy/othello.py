
import sys
sys.stdin = open("input.txt")

def in_range(n, r, c):                  # 범위 n 안에서 탐색
    return 0 <= r < n and 0 <= c < n

def hor(board, r, c, color):            # 
    n = len(board)
    opp = 2 if color == 1 else 1        # 상대 2, if 내가 1 else 나 2 상대 1

    # right
    captured = []
    cc = c + 1
    while in_range(n, r, cc) and board[r][cc] == opp:
        captured.append((r, cc))
        cc += 1
    if in_range(n, r, cc) and board[r][cc] == color:
        for rr, cc in captured:
            board[rr][cc] = color

    # left
    captured = []
    cc = c - 1
    while in_range(n, r, cc) and board[r][cc] == opp:
        captured.append((r, cc))
        cc -= 1
    if in_range(n, r, cc) and board[r][cc] == color:
        for rr, cc in captured:
            board[rr][cc] = color


def ver(board, r, c, color):
    n = len(board)
    opp = 2 if color == 1 else 1

    # down
    captured = []
    rr = r + 1
    while in_range(n, rr, c) and board[rr][c] == opp:
        captured.append((rr, c))
        rr += 1
    if in_range(n, rr, c) and board[rr][c] == color:
        for rr, cc in captured:
            board[rr][cc] = color

    # up
    captured = []
    rr = r - 1
    while in_range(n, rr, c) and board[rr][c] == opp:
        captured.append((rr, c))
        rr -= 1
    if in_range(n, rr, c) and board[rr][c] == color:
        for rr, cc in captured:
            board[rr][cc] = color


def diag(board, r, c, color):
    n = len(board)
    opp = 2 if color == 1 else 1
    dirs = [(-1,-1), (-1,1), (1,-1), (1,1)]  # 2nd 1st 3rd 4th

    for dr, dc in dirs:
        captured = []
        rr, cc = r + dr, c + dc
        while in_range(n, rr, cc) and board[rr][cc] == opp:
            captured.append((rr, cc))
            rr += dr
            cc += dc
        if in_range(n, rr, cc) and board[rr][cc] == color:
            for cr, cc in captured:
                board[cr][cc] = color


t = int(input())
for tc in range(1, 1 + t):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]

    # 초기 배치
    mid = n // 2
    board[mid][mid] = 2
    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1

    for _ in range(m):
        x, y, color = map(int, input().split())
        r, c = y-1, x-1  # 입력은 1-index
        board[r][c] = color  # 돌 놓기

        hor(board, r, c, color)
        ver(board, r, c, color)
        diag(board, r, c, color)

    black = sum(row.count(1) for row in board)
    white = sum(row.count(2) for row in board)
    print(f"#{tc} {black} {white}")



