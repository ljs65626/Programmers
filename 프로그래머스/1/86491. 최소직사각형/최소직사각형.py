import sys
def solution(sizes):
    answer = 0
    leng = len(sizes)
    for i in range(leng):
        a, b = sizes[i]
        sizes[i][0], sizes[i][1] = max(a, b), min(a, b)
    
    maxa = -sys.maxsize
    maxb = -sys.maxsize
    for i in range(leng):
        a, b = sizes[i]
        maxa = max(a, maxa)
        maxb = max(b, maxb)
    answer = maxa*maxb
    return answer