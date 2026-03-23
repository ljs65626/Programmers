import sys
def solution(sequence, k):
    leng = len(sequence)
    left=0
    right=0
    sum_val=sequence[0]
    answer=[]
    min_length = sys.maxsize
    while left<=right and right<leng:
        if sum_val>k:
            sum_val-=sequence[left]
            left+=1
        elif sum_val<k:
            right+=1
            if right<leng:
                sum_val+=sequence[right]
        else:
            if right - left < min_length:
                min_length = right - left
                answer = [left, right]
            sum_val -= sequence[left]
            left += 1
    return answer