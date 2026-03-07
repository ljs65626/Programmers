def solution(s):
    answer = []
    leng = len(s)
    for i in range(leng):
        is_satisfied=False
        for j in range(i):
            if s[i]==s[j]:
                is_satisfied=True
                big = j
                # answer.append(i-j)
        if not is_satisfied:
            answer.append(-1)
        else:
            answer.append(i-big)
            
    return answer