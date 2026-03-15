def solution(food):
    answer = ''
    leng = len(food)
    for i in range(1, leng):
        for j in range(food[i]//2):
            answer+= str(i)
    
    answer = answer + '0' + "".join(reversed(answer))
    return answer