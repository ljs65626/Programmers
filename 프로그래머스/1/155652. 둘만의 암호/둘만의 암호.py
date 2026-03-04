def solution(s, skip, index):
    answer = []
    for i in s:
        temp = ord(i)
        for _ in range(index):
            issatisfied=False
            temp += 1
            while not issatisfied:
            
                if temp>ord('z'):
                    temp = ord('a')
            
                if chr(temp) in skip:
                    temp+=1
                    if temp>ord('z'):
                        temp = ord('a')
                else:
                    issatisfied=True
                
        answer.append(chr(temp))
    return ''.join(answer)