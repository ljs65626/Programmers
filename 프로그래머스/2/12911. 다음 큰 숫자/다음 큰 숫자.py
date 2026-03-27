def two(num):
    cnt=0
    while num!=1:
        if num%2==1:
            cnt+=1
        num//=2
    
    return cnt

def solution(n):
    answer = 0
    n_cnt = two(n)
    for i in range(n+1, 2000000):
        i_cnt = two(i)
        if i_cnt==n_cnt:
            answer=i
            break
    return answer