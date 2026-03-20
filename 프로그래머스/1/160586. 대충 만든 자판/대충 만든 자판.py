def solution(keymap, targets):
    answer = []
    for target in targets:
        ans=0
        for t in target:
            min_index = 101
            finding=False
            for key in keymap:
                if key.find(t)!=-1:
                    finding=True
                    min_index = min(key.find(t), min_index)
            if finding==True:
                ans+=(min_index+1)
            else:
                ans=-1
                break
        answer.append(ans)
    return answer