def solution(cards1, cards2, goal):
    answer = ''
    is_satisfied=True
    arrow1=0
    arrow2=0
    len1 = len(cards1)
    len2 = len(cards2)
    for i in goal:
        if arrow1<len1 and i == cards1[arrow1]:
            is_satisfied=True
            arrow1+=1
        else:
            is_satisfied=False

        if not is_satisfied and arrow2<len2:
            if i == cards2[arrow2]:
                is_satisfied=True
                arrow2+=1
            else:
                is_satisfied=False
        
        if is_satisfied==False:
            break
    
    if is_satisfied:
        answer='Yes'
    else:
        answer='No'

    return answer