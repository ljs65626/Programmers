arr=[]
answer=-1
visited=[False]*8

def func(k, dungeons):
    cnt=0
    temp = k
    for i in arr:
        if temp>=dungeons[i][0]:
            cnt+=1
            temp-=dungeons[i][1]
        else:
            break
    return cnt

def backtrack(curr_loc, k, dungeons):
    global answer
    leng = len(dungeons)
    if curr_loc==leng:
        answer = max(answer, func(k, dungeons))
        return
    
    for i in range(leng):
        if visited[i]==True:
            continue
        visited[i]=True
        arr.append(i)
        backtrack(curr_loc+1, k, dungeons)
        arr.pop()
        visited[i]=False

def solution(k, dungeons):
    global answer
    backtrack(0, k, dungeons)
    return answer
