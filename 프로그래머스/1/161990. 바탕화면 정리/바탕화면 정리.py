import sys

def solution(wallpaper):
    answer = []
    w = len(wallpaper)
    h = len(wallpaper[0])
    smallest_x=sys.maxsize
    biggest_x=-sys.maxsize
    smallest_y=sys.maxsize
    biggest_y=-sys.maxsize
    for i in range(w):
        for j in range(h):
            if wallpaper[i][j]=='#':
                smallest_x = min(i, smallest_x)
                smallest_y = min(j, smallest_y)
                biggest_x = max(i, biggest_x)
                biggest_y = max(j, biggest_y)
                
    answer=[smallest_x, smallest_y, biggest_x+1, biggest_y+1]
                    
    return answer