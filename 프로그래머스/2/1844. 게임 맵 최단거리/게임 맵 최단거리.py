from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    score = [[0 for _ in range(m)] for _ in range(n)]
    answer = 0
    
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    q = deque()
    
    def push(x, y, v):
        visited[x][y]=True
        q.append((x, y))
        score[x][y] = v

    def in_range(x, y, maps):
        if x>=0 and x<n and y>=0 and y<m:
            return True
        else:
            return False

    def can_go(x, y, maps):
        if not in_range(x, y, maps):
            return False
        if visited[x][y]==True:
            return False
        if maps[x][y]==0:
            return False
        return True

    def bfs(maps):
        while q:
            x, y = q.popleft()
            for dx, dy in zip(dxs, dys):
                new_x = x+dx
                new_y = y+dy
                if can_go(new_x, new_y, maps):
                    push(new_x, new_y, score[x][y]+1)
    
    push(0, 0, 1)
    bfs(maps)
    if visited[n-1][m-1]:
        answer = score[n-1][m-1]
    else:
        answer = -1
    return answer