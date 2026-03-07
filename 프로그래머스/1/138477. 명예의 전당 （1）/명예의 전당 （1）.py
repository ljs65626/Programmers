
def solution(k, score):
    answer = []
    oner = []
    leng = len(score)
    if k<=leng:
        for i in range(k):
            oner.append(score[i])
            answer.append(min(oner))
    else:
        for i in range(leng):
            oner.append(score[i])
            answer.append(min(oner))
            
        
    for i in range(k, leng):
        oner.sort()
        if oner[0]<score[i]:
            oner.append(score[i])
            oner.pop(0)
        answer.append(min(oner))
        
        
    return answer