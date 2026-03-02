def solution(t, p):
    answer = 0
    lent = len(t)
    lenp = len(p)
    tempp = int(p)
    for i in range(lent-lenp+1):
        tempt = t[i:i+lenp]
        tempt = int(tempt)
        
        if tempt<=tempp:
            answer+=1
    return answer