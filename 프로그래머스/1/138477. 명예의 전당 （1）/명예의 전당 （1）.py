
def solution(k, score):
    answer = []
#     oner = []
#     leng = len(score)
#     if k<=leng:
#         for i in range(k):
#             oner.append(score[i])
#             answer.append(min(oner))
#     else:
#         for i in range(leng):
#             oner.append(score[i])
#             answer.append(min(oner))
            
        
#     for i in range(k, leng):
#         oner.sort()
#         if oner[0]<score[i]:
#             oner.append(score[i])
#             oner.pop(0)
#         answer.append(min(oner))
    
    q=[]
    for s in score:
        q.append(s)
        if len(q)>k:
            q.remove(min(q))
        answer.append(min(q))
        
    return answer