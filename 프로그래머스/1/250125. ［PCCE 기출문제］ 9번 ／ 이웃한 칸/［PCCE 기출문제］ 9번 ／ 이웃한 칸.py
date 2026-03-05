def in_range(x, y, n):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def solution(board, h, w):
    answer = 0
    n = len(board)
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    
    for dx, dy in zip(dxs, dys):
        if in_range(h+dx, w+dy, n):
            if board[h+dx][w+dy]==board[h][w]:
                answer+=1
    return answer