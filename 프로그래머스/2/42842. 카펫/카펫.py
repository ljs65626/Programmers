def solution(brown, yellow):
    answer = []
    
    for x in range(1, 2500):
        y = ((brown+4)//2)-x
        if x>=y and x*y==(brown+yellow):
            answer.append([x,y])
    return answer[0]