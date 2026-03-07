def solution(bandage, health, attacks):
    answer = 0
    current=health
    leng = len(attacks)
    for i in range(leng):
        attack_time1, damage1 = attacks[i]
        
        if i==0:
            current-=damage1
            if current<=0:
                answer=-1
                return answer
            continue
            
        attack_time2, damage2 = attacks[i-1]
        diff = attack_time1-attack_time2
        if diff > bandage[0]:
            current+=((diff*bandage[1])+(bandage[2]*((diff-1)//bandage[0]))-bandage[1])
        else:
            current+=((diff-1)*bandage[1])
        
        current = min(health, current)
        current-=damage1
        if current<=0:
            answer=-1
            return answer
    
    answer=current
                
        
    return answer