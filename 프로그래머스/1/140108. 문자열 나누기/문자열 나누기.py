def solution(s):
    answer = 0
    leng = len(s)
    first=0
    iterater=0
    x_cnt=0
    nonx_cnt=0
    while first<leng:
        if s[iterater]==s[first]:
            x_cnt+=1
        else:
            nonx_cnt+=1
        
        iterater+=1
        if iterater>=leng:
            answer+=1
            break
        if x_cnt==nonx_cnt:
            first = iterater
            answer+=1
            x_cnt=0
            nonx_cnt=0
        
    return answer